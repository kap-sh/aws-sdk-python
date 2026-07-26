"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyTemplateFilterName``."""

from typing import TypeAlias

"""<p>The filter name for filtering notify templates. The available filter names are:</p> <ul> <li> <p> <code>channels</code>: Filter by channels.</p> </li> <li> <p> <code>language-code</code>: Filter by language code.</p> </li> <li> <p> <code>supported-countries</code>: Filter by supported countries.</p> </li> <li> <p> <code>supported-voice-ids</code>: Filter by supported voice IDs.</p> </li> <li> <p> <code>template-type</code>: Filter by template type.</p> </li> <li> <p> <code>tier-access</code>: Filter by tier access.</p> </li> </ul>"""
NotifyTemplateFilterName: TypeAlias = str
