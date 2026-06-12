"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ProfileVisibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

ProfileVisibility: TypeAlias = Literal[
    "PRIVATE",
    "PUBLIC",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIVATE",
        "PUBLIC",
    )
)


def serialize_aws_json_1_0(value: ProfileVisibility) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProfileVisibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileVisibility value: {data!r}")
    return cast(ProfileVisibility, data)
