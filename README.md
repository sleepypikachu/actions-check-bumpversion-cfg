# Check bumpversion Config Action

This action checks your `.bumpversion.cfg` contains a `current_version` key and a `new_version` key which is set to a later version.

# Example usage

```yaml
uses: sleepypikachu/actions-check-bumpversion-cfg@v1.0.0
```

Enforces that you have a `.bumpversion.cfg` like
```cfg
[bumpversion]
current_version = 1.0.0
new_version = 1.0.1
```

Example configs which would fail this check

```cfg
[bumpversion]
current_version = 1.0.0
```

```cfg
[bumpversion]
new_version = 1.0.0
```

```cfg
[bumpversion]
current_version = 3.0.0
new_version = 2.1.0
```

