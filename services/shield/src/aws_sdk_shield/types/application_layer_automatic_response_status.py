"""Generated from Smithy shape ``com.amazonaws.shield#ApplicationLayerAutomaticResponseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

ApplicationLayerAutomaticResponseStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ApplicationLayerAutomaticResponseStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationLayerAutomaticResponseStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ApplicationLayerAutomaticResponseStatus value: {data!r}"
        )
    return cast(ApplicationLayerAutomaticResponseStatus, data)
