"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.list_links_response_structure

LinkList: TypeAlias = list[
    "aws_sdk_rtbfabric.types.list_links_response_structure.ListLinksResponseStructure"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkList) -> list:
    import aws_sdk_rtbfabric.types.list_links_response_structure

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rtbfabric.types.list_links_response_structure.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LinkList:
    import aws_sdk_rtbfabric.types.list_links_response_structure

    out: LinkList = []
    for item in data:
        out.append(
            aws_sdk_rtbfabric.types.list_links_response_structure.deserialize_json(item)
        )
    return out
