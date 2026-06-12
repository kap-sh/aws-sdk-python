"""Generated from Smithy shape ``com.amazonaws.fms#ListProtocolsListsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.pagination_token
    import aws_sdk_fms.types.protocols_lists_data


class ListProtocolsListsResponse(TypedDict):
    protocols_lists: NotRequired[
        "aws_sdk_fms.types.protocols_lists_data.ProtocolsListsData"
    ]
    """<p>An array of <code>ProtocolsListDataSummary</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_fms.types.pagination_token.PaginationToken"]
    """<p>If you specify a value for <code>MaxResults</code> in your list request, and you have more objects than the maximum, Firewall Manager returns this token in the response. You can use this token in subsequent requests to retrieve the next batch of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProtocolsListsResponse) -> dict:
    out: dict = {}
    if "protocols_lists" in value:
        import aws_sdk_fms.types.protocols_lists_data

        out["ProtocolsLists"] = (
            aws_sdk_fms.types.protocols_lists_data.serialize_aws_json_1_1(
                value["protocols_lists"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProtocolsListsResponse:
    out: ListProtocolsListsResponse = {}  # type: ignore[typeddict-item]
    if "ProtocolsLists" in data:
        import aws_sdk_fms.types.protocols_lists_data

        out["protocols_lists"] = (
            aws_sdk_fms.types.protocols_lists_data.deserialize_aws_json_1_1(
                data["ProtocolsLists"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
