"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListLunaClientsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.pagination_token


class ListLunaClientsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cloudhsm.types.pagination_token.PaginationToken"]
    """<p>The <code>NextToken</code> value from a previous call to <code>ListLunaClients</code>. Pass null if this is the first call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLunaClientsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLunaClientsRequest:
    out: ListLunaClientsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
