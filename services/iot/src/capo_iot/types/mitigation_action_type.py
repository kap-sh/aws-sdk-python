"""Generated from Smithy shape ``com.amazonaws.iot#MitigationActionType``."""

from typing import Literal, TypeAlias, cast

MitigationActionType: TypeAlias = Literal[
    "UPDATE_DEVICE_CERTIFICATE",
    "UPDATE_CA_CERTIFICATE",
    "ADD_THINGS_TO_THING_GROUP",
    "REPLACE_DEFAULT_POLICY_VERSION",
    "ENABLE_IOT_LOGGING",
    "PUBLISH_FINDING_TO_SNS",
]


# --- restJson1 ser/de ---
def serialize_json(value: MitigationActionType) -> str:
    return value


def deserialize_json(data: str) -> MitigationActionType:
    return cast(MitigationActionType, data)
