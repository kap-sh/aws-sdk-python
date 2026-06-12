"""Generated from Smithy shape ``com.amazonaws.iot#MitigationActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

MitigationActionType: TypeAlias = Literal[
    "UPDATE_DEVICE_CERTIFICATE",
    "UPDATE_CA_CERTIFICATE",
    "ADD_THINGS_TO_THING_GROUP",
    "REPLACE_DEFAULT_POLICY_VERSION",
    "ENABLE_IOT_LOGGING",
    "PUBLISH_FINDING_TO_SNS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATE_DEVICE_CERTIFICATE",
        "UPDATE_CA_CERTIFICATE",
        "ADD_THINGS_TO_THING_GROUP",
        "REPLACE_DEFAULT_POLICY_VERSION",
        "ENABLE_IOT_LOGGING",
        "PUBLISH_FINDING_TO_SNS",
    )
)


def serialize_json(value: MitigationActionType) -> str:
    return value


def deserialize_json(data: str) -> MitigationActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MitigationActionType value: {data!r}")
    return cast(MitigationActionType, data)
