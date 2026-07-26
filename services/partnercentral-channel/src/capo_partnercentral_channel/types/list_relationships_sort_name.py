"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListRelationshipsSortName``."""

from typing import Literal, TypeAlias, cast

ListRelationshipsSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRelationshipsSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListRelationshipsSortName:
    return cast(ListRelationshipsSortName, data)
