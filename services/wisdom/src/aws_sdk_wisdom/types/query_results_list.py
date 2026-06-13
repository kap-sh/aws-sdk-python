"""Generated from Smithy shape ``com.amazonaws.wisdom#QueryResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.result_data

QueryResultsList: TypeAlias = list["aws_sdk_wisdom.types.result_data.ResultData"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryResultsList) -> list:
    import aws_sdk_wisdom.types.result_data

    out: list = []
    for item in value:
        out.append(aws_sdk_wisdom.types.result_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryResultsList:
    import aws_sdk_wisdom.types.result_data

    out: QueryResultsList = []
    for item in data:
        out.append(aws_sdk_wisdom.types.result_data.deserialize_json(item))
    return out
