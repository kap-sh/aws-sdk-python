"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectAccessLoggingFormat``."""

from typing import Literal, TypeAlias

"""<p>The format for Service Connect access log output. Choose TEXT for human-readable logs or JSON for structured data that integrates well with log analysis tools.</p>"""
ServiceConnectAccessLoggingFormat: TypeAlias = Literal[
    "TEXT",
    "JSON",
]
