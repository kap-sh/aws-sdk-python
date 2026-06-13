module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'scope-enum': [0],
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'fix',
        'docs',
        'chore',
        'refactor',
        'test',
        'revert',
        'ci',
        'build',
        'perf',
        'style'
      ]
    ],
    'subject-case': [2, 'never', ['start-case', 'pascal-case', 'upper-case']],
    'header-max-length': [2, 'always', 100]
  }
};
