%if actual is None:
    not firefox
%else:
    expected firefox version {{expected}}, got {{actual}}
%end
