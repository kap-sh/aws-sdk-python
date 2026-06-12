"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.search_resource_type

SearchResourceTypeList: TypeAlias = list[
    "aws_sdk_workdocs.types.search_resource_type.SearchResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourceTypeList) -> list:
    import aws_sdk_workdocs.types.search_resource_type

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.search_resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchResourceTypeList:
    import aws_sdk_workdocs.types.search_resource_type

    out: SearchResourceTypeList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.search_resource_type.deserialize_json(item))
    return out
