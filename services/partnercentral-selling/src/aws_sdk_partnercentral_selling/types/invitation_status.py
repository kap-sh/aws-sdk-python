"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#InvitationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

InvitationStatus: TypeAlias = Literal[
    "ACCEPTED",
    "PENDING",
    "REJECTED",
    "EXPIRED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCEPTED",
        "PENDING",
        "REJECTED",
        "EXPIRED",
    )
)


def serialize_aws_json_1_0(value: InvitationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvitationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvitationStatus value: {data!r}")
    return cast(InvitationStatus, data)
