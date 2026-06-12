"""Generated from Smithy shape ``com.amazonaws.wafregional#GetWebACLRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_id


class GetWebACLRequest(TypedDict):
    web_acl_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>WebACLId</code> of the <a>WebACL</a> that you want to get. <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWebACLRequest:
    out: GetWebACLRequest = {}  # type: ignore[typeddict-item]
    if "WebACLId" in data:
        out["web_acl_id"] = data["WebACLId"]
    else:
        raise DeserializationError("GetWebACLRequest.web_acl_id required")
    return out
