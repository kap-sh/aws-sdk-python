"""Generated from Smithy shape ``com.amazonaws.wafregional#DeleteByteMatchSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.resource_id


class DeleteByteMatchSetRequest(TypedDict):
    byte_match_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>ByteMatchSetId</code> of the <a>ByteMatchSet</a> that you want to delete. <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteByteMatchSetRequest) -> dict:
    out: dict = {}
    out["ByteMatchSetId"] = value["byte_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteByteMatchSetRequest:
    out: DeleteByteMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "ByteMatchSetId" in data:
        out["byte_match_set_id"] = data["ByteMatchSetId"]
    else:
        raise DeserializationError(
            "DeleteByteMatchSetRequest.byte_match_set_id required"
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteByteMatchSetRequest.change_token required")
    return out
