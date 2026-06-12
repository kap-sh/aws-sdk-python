"""Generated from Smithy shape ``com.amazonaws.resourcegroups#QueryErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.query_error

QueryErrorList: TypeAlias = list["aws_sdk_resource_groups.types.query_error.QueryError"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryErrorList) -> list:
    import aws_sdk_resource_groups.types.query_error

    out: list = []
    for item in value:
        out.append(aws_sdk_resource_groups.types.query_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryErrorList:
    import aws_sdk_resource_groups.types.query_error

    out: QueryErrorList = []
    for item in data:
        out.append(aws_sdk_resource_groups.types.query_error.deserialize_json(item))
    return out
