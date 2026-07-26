"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementSortName``."""

from typing import Literal, TypeAlias, cast

EngagementSortName: TypeAlias = Literal["CreatedDate",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngagementSortName:
    return cast(EngagementSortName, data)
