"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityOrigin``."""

from typing import Literal, TypeAlias, cast

OpportunityOrigin: TypeAlias = Literal[
    "AWS Referral",
    "Partner Referral",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunityOrigin) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpportunityOrigin:
    return cast(OpportunityOrigin, data)
