"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListTasksSortName``."""

from typing import Literal, TypeAlias, cast

ListTasksSortName: TypeAlias = Literal["StartTime",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTasksSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListTasksSortName:
    return cast(ListTasksSortName, data)
