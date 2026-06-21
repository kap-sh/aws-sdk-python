"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectAccessLoggingFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The format for Service Connect access log output. Choose TEXT for human-readable logs or JSON for structured data that integrates well with log analysis tools.</p>"""
ServiceConnectAccessLoggingFormat: TypeAlias = Literal[
    "TEXT",
    "JSON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectAccessLoggingFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceConnectAccessLoggingFormat:
    return cast(ServiceConnectAccessLoggingFormat, data)
