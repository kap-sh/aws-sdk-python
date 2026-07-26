"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListResponseScope``."""

from typing import Literal, TypeAlias, cast

ListResponseScope: TypeAlias = Literal["METADATA_ONLY",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResponseScope) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListResponseScope:
    return cast(ListResponseScope, data)
