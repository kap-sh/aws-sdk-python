"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListIndexesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.index_list


class ListIndexesOutput(TypedDict):
    indexes: NotRequired["aws_sdk_resource_explorer_2.types.index_list.IndexList"]
    """<p>A structure that contains the details and status of each index.</p>"""
    next_token: NotRequired["str"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. The pagination tokens expire after 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexesOutput) -> dict:
    out: dict = {}
    if "indexes" in value:
        import aws_sdk_resource_explorer_2.types.index_list

        out["Indexes"] = aws_sdk_resource_explorer_2.types.index_list.serialize_json(
            value["indexes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIndexesOutput:
    out: ListIndexesOutput = {}  # type: ignore[typeddict-item]
    if "Indexes" in data:
        import aws_sdk_resource_explorer_2.types.index_list

        out["indexes"] = aws_sdk_resource_explorer_2.types.index_list.deserialize_json(
            data["Indexes"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
