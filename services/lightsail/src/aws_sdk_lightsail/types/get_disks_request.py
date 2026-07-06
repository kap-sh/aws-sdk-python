"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDisksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string


class GetDisksRequest(TypedDict, closed=True):
    page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetDisks</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDisksRequest) -> dict:
    out: dict = {}
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDisksRequest:
    out: GetDisksRequest = {}  # type: ignore[typeddict-item]
    if "pageToken" in data:
        out["page_token"] = data["pageToken"]
    return out
