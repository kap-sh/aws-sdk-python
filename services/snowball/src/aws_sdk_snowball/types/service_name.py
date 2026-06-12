"""Generated from Smithy shape ``com.amazonaws.snowball#ServiceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

ServiceName: TypeAlias = Literal[
    "KUBERNETES",
    "EKS_ANYWHERE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KUBERNETES",
        "EKS_ANYWHERE",
    )
)


def serialize_aws_json_1_1(value: ServiceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceName value: {data!r}")
    return cast(ServiceName, data)
