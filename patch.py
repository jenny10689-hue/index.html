with open('khhplaza.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 把「清除上班日」按鈕改成「清除自動排班」
old1 = """      <button class="ibtn" id="clear-work-btn" style="color:#A32D2D">🗑 清除上班日</button>"""
new1 = """      <button class="ibtn" id="clear-auto-btn" style="color:#A32D2D">🗑 清除自動排班</button>"""

if old1 in content:
    content = content.replace(old1, new1, 1)
    print('✓ 按鈕改名')
else:
    print('✗ 按鈕找不到')

# 2. 把 clear-work-btn 事件改成 clear-auto-btn，並修改邏輯（清除所有非手動格）
old2 = """document.getElementById('clear-work-btn').addEventListener('click', () => {
  if (!confirm('清除所有人的上班日（保留假別）？')) return;
  pushHistory('清除上班日', null);
  const days = daysInMonth(state.year, state.month);
  state.staff.forEach(s => {
    for (let d = 1; d <= days; d++) {
      const key = cellKey(s.id, d);
      const v = state.cells[key] || '';
      if (isWork(v)) {
        delete state.cells[key];
        state.edited.delete(key);
      }
    }
  });
  state.unsaved = true;
  setSaveStatus('有未儲存的變更');
  renderTable(); renderStats(); renderWarnings();
  showToast('已清除所有上班日');
});"""
new2 = """document.getElementById('clear-auto-btn').addEventListener('click', () => {
  if (!confirm('清除所有自動排班格子（保留手動畫格）？')) return;
  pushHistory('清除自動排班', null);
  const days = daysInMonth(state.year, state.month);
  state.staff.forEach(s => {
    for (let d = 1; d <= days; d++) {
      const key = cellKey(s.id, d);
      if (!state.edited.has(key)) {
        delete state.cells[key];
      }
    }
  });
  state.unsaved = true;
  setSaveStatus('有未儲存的變更');
  renderTable(); renderStats(); renderWarnings();
  showToast('已清除自動排班');
});"""

if old2 in content:
    content = content.replace(old2, new2, 1)
    print('✓ 事件邏輯更新')
else:
    print('✗ 事件找不到')

with open('khhplaza.html', 'w', encoding='utf-8') as f:
    f.write(content)
