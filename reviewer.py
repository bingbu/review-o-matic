  MAX_CONTEXT = 5

  def __strip_kruft(self, diff, context):
              LineType.RENAME, LineType.EMPTY]
    ctx_counter = 0
        ctx_counter = 0
        continue

      if l_type == LineType.CONTEXT:
        if ctx_counter < context:
          ret.append(l)
        ctx_counter += 1
        continue

      ctx_counter = 0

      if l_type in ignore:
      else:
        sys.stderr.write('ERROR: line_type not handled {}: {}\n'.format(l_type,
                                                                        l))

    cmd = self.git_cmd + ['show', '--minimal', '-U{}'.format(self.MAX_CONTEXT),
                          r'--format=%B', sha]
  def compare_diffs(self, a, b, context=0):
    if context > self.MAX_CONTEXT:
      raise ValueError('Invalid context given')

    a = self.__strip_kruft(a, context)
    b = self.__strip_kruft(b, context)