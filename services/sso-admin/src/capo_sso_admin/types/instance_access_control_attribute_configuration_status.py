"""Generated from Smithy shape ``com.amazonaws.ssoadmin#InstanceAccessControlAttributeConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

InstanceAccessControlAttributeConfigurationStatus: TypeAlias = Literal[
    "ENABLED",
    "CREATION_IN_PROGRESS",
    "CREATION_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InstanceAccessControlAttributeConfigurationStatus,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> InstanceAccessControlAttributeConfigurationStatus:
    return cast(InstanceAccessControlAttributeConfigurationStatus, data)
