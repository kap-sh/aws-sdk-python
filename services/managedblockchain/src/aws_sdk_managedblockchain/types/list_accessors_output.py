"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListAccessorsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.accessor_summary_list
    import aws_sdk_managedblockchain.types.pagination_token


class ListAccessorsOutput(TypedDict):
    accessors: NotRequired[
        "aws_sdk_managedblockchain.types.accessor_summary_list.AccessorSummaryList"
    ]
    """<p>An array of AccessorSummary objects that contain configuration properties for each accessor.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p> The pagination token that indicates the next set of results to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessorsOutput) -> dict:
    out: dict = {}
    if "accessors" in value:
        import aws_sdk_managedblockchain.types.accessor_summary_list

        out["Accessors"] = (
            aws_sdk_managedblockchain.types.accessor_summary_list.serialize_json(
                value["accessors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessorsOutput:
    out: ListAccessorsOutput = {}  # type: ignore[typeddict-item]
    if "Accessors" in data:
        import aws_sdk_managedblockchain.types.accessor_summary_list

        out["accessors"] = (
            aws_sdk_managedblockchain.types.accessor_summary_list.deserialize_json(
                data["Accessors"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
