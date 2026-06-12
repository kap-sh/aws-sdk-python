"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityEngagementInvitationSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

OpportunityEngagementInvitationSortName: TypeAlias = Literal["InvitationDate",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("InvitationDate",))


def serialize_aws_json_1_0(value: OpportunityEngagementInvitationSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpportunityEngagementInvitationSortName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OpportunityEngagementInvitationSortName value: {data!r}"
        )
    return cast(OpportunityEngagementInvitationSortName, data)
