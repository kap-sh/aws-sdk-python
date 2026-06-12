"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementInvitationPayloadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

EngagementInvitationPayloadType: TypeAlias = Literal[
    "OpportunityInvitation",
    "LeadInvitation",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OpportunityInvitation",
        "LeadInvitation",
    )
)


def serialize_aws_json_1_0(value: EngagementInvitationPayloadType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngagementInvitationPayloadType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EngagementInvitationPayloadType value: {data!r}"
        )
    return cast(EngagementInvitationPayloadType, data)
