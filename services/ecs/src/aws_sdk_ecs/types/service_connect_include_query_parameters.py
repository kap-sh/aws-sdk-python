"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectIncludeQueryParameters``."""

from typing import Literal, TypeAlias

"""<p>Controls whether query parameters are included in Service Connect access logs. Consider security and privacy implications when enabling this feature. By default, this parameter is <code>DISABLED</code>.</p>"""
ServiceConnectIncludeQueryParameters: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]
