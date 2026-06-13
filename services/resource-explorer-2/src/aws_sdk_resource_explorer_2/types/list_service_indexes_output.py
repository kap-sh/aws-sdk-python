"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListServiceIndexesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.index_list


class ListServiceIndexesOutput(TypedDict):
    indexes: NotRequired["aws_sdk_resource_explorer_2.types.index_list.IndexList"]
    """<p>A list of <code>Index</code> objects that describe the Resource Explorer indexes found in the specified Regions.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token to use in a subsequent <code>ListServiceIndexes</code> request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceIndexesOutput) -> dict:
    out: dict = {}
    if "indexes" in value:
        import aws_sdk_resource_explorer_2.types.index_list

        out["Indexes"] = aws_sdk_resource_explorer_2.types.index_list.serialize_json(
            value["indexes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceIndexesOutput:
    out: ListServiceIndexesOutput = {}  # type: ignore[typeddict-item]
    if "Indexes" in data:
        import aws_sdk_resource_explorer_2.types.index_list

        out["indexes"] = aws_sdk_resource_explorer_2.types.index_list.deserialize_json(
            data["Indexes"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
