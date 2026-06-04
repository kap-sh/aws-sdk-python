"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectIncludeQueryParameters``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

"""<p>Controls whether query parameters are included in Service Connect access logs. Consider security and privacy implications when enabling this feature. By default, this parameter is <code>DISABLED</code>.</p>"""
ServiceConnectIncludeQueryParameters: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_aws_json_1_1(value: ServiceConnectIncludeQueryParameters) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceConnectIncludeQueryParameters:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceConnectIncludeQueryParameters value: {data!r}"
        )
    return cast(ServiceConnectIncludeQueryParameters, data)
