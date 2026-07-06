"""Generated from Smithy shape ``com.amazonaws.lightsail#GetKeyPairsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.string


class GetKeyPairsRequest(TypedDict, closed=True):
    page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetKeyPairs</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""
    include_default_key_pair: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether to include the default key pair in the response of your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyPairsRequest) -> dict:
    out: dict = {}
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    if "include_default_key_pair" in value:
        out["includeDefaultKeyPair"] = value["include_default_key_pair"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyPairsRequest:
    out: GetKeyPairsRequest = {}  # type: ignore[typeddict-item]
    if "pageToken" in data:
        out["page_token"] = data["pageToken"]
    if "includeDefaultKeyPair" in data:
        out["include_default_key_pair"] = data["includeDefaultKeyPair"]
    return out
