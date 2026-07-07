"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListHapgsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.pagination_token


class ListHapgsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cloudhsm.types.pagination_token.PaginationToken"]
    """<p>The <code>NextToken</code> value from a previous call to <code>ListHapgs</code>. Pass null if this is the first call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHapgsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHapgsRequest:
    out: ListHapgsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
