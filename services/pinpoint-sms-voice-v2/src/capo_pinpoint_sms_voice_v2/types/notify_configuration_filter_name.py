"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyConfigurationFilterName``."""

from typing import TypeAlias

"""<p>The filter name for filtering notify configurations. The available filter names are:</p> <ul> <li> <p> <code>default-pool</code>: Filter by the default pool.</p> </li> <li> <p> <code>default-template</code>: Filter by the default template.</p> </li> <li> <p> <code>deletion-protection-enabled</code>: Filter by deletion protection status.</p> </li> <li> <p> <code>display-name</code>: Filter by display name.</p> </li> <li> <p> <code>enabled-channels</code>: Filter by enabled channels.</p> </li> <li> <p> <code>enabled-countries</code>: Filter by enabled countries.</p> </li> <li> <p> <code>status</code>: Filter by status.</p> </li> <li> <p> <code>tier-upgrade-status</code>: Filter by tier upgrade status.</p> </li> <li> <p> <code>use-case</code>: Filter by use case.</p> </li> </ul>"""
NotifyConfigurationFilterName: TypeAlias = str
