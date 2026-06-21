"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySortName``."""

from typing import Literal, TypeAlias, cast

OpportunitySortName: TypeAlias = Literal[
    "LastModifiedDate",
    "Identifier",
    "CustomerCompanyName",
    "CreatedDate",
    "TargetCloseDate",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunitySortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpportunitySortName:
    return cast(OpportunitySortName, data)
