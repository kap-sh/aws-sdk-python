"""Generated from Smithy shape ``com.amazonaws.storagegateway#Squash``."""

from typing import TypeAlias

"""<p>The user mapped to anonymous user. Valid options are the following:</p> <ul> <li> <p> <code>RootSquash</code>: Only root is mapped to anonymous user.</p> </li> <li> <p> <code>NoSquash</code>: No one is mapped to anonymous user.</p> </li> <li> <p> <code>AllSquash</code>: Everyone is mapped to anonymous user.</p> </li> </ul>"""
Squash: TypeAlias = str
