"""Generated from Smithy shape ``com.amazonaws.workmail#PersonalAccessTokenConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

PersonalAccessTokenConfigurationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: PersonalAccessTokenConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PersonalAccessTokenConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PersonalAccessTokenConfigurationStatus value: {data!r}"
        )
    return cast(PersonalAccessTokenConfigurationStatus, data)
