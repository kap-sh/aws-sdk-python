"""Generated from Smithy shape ``com.amazonaws.directconnect#ListVirtualInterfaceTestHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.pagination_token
    import aws_sdk_direct_connect.types.virtual_interface_test_history_list


class ListVirtualInterfaceTestHistoryResponse(TypedDict, closed=True):
    virtual_interface_test_history: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_test_history_list.VirtualInterfaceTestHistoryList"
    ]
    """<p>The ID of the tested virtual interface.</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVirtualInterfaceTestHistoryResponse) -> dict:
    out: dict = {}
    if "virtual_interface_test_history" in value:
        import aws_sdk_direct_connect.types.virtual_interface_test_history_list

        out["virtualInterfaceTestHistory"] = (
            aws_sdk_direct_connect.types.virtual_interface_test_history_list.serialize_aws_json_1_1(
                value["virtual_interface_test_history"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVirtualInterfaceTestHistoryResponse:
    out: ListVirtualInterfaceTestHistoryResponse = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceTestHistory" in data:
        import aws_sdk_direct_connect.types.virtual_interface_test_history_list

        out["virtual_interface_test_history"] = (
            aws_sdk_direct_connect.types.virtual_interface_test_history_list.deserialize_aws_json_1_1(
                data["virtualInterfaceTestHistory"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
