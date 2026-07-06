"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListLunaClientsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.client_list
    import aws_sdk_cloudhsm.types.pagination_token


class ListLunaClientsResponse(TypedDict, closed=True):
    client_list: "aws_sdk_cloudhsm.types.client_list.ClientList"
    """<p>The list of clients.</p>"""
    next_token: NotRequired["aws_sdk_cloudhsm.types.pagination_token.PaginationToken"]
    """<p>If not null, more results are available. Pass this to <code>ListLunaClients</code> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLunaClientsResponse) -> dict:
    out: dict = {}
    import aws_sdk_cloudhsm.types.client_list

    out["ClientList"] = aws_sdk_cloudhsm.types.client_list.serialize_aws_json_1_1(
        value["client_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLunaClientsResponse:
    out: ListLunaClientsResponse = {}  # type: ignore[typeddict-item]
    if "ClientList" in data:
        import aws_sdk_cloudhsm.types.client_list

        out["client_list"] = (
            aws_sdk_cloudhsm.types.client_list.deserialize_aws_json_1_1(
                data["ClientList"]
            )
        )
    else:
        raise DeserializationError("ListLunaClientsResponse.client_list required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
