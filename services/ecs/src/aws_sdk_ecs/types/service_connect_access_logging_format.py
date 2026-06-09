"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectAccessLoggingFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

"""<p>The format for Service Connect access log output. Choose TEXT for human-readable logs or JSON for structured data that integrates well with log analysis tools.</p>"""
ServiceConnectAccessLoggingFormat: TypeAlias = Literal[
    "TEXT",
    "JSON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "JSON",
    )
)


def serialize_aws_json_1_1(value: ServiceConnectAccessLoggingFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceConnectAccessLoggingFormat:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceConnectAccessLoggingFormat value: {data!r}"
        )
    return cast(ServiceConnectAccessLoggingFormat, data)
