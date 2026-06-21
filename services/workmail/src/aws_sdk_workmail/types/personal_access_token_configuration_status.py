"""Generated from Smithy shape ``com.amazonaws.workmail#PersonalAccessTokenConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

PersonalAccessTokenConfigurationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonalAccessTokenConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PersonalAccessTokenConfigurationStatus:
    return cast(PersonalAccessTokenConfigurationStatus, data)
