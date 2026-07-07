"""Generated from Smithy shape ``com.amazonaws.wafregional#WebACLSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.resource_name


class WebACLSummary(TypedDict, closed=True):
    web_acl_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>WebACL</code>. You use <code>WebACLId</code> to get information about a <code>WebACL</code> (see <a>GetWebACL</a>), update a <code>WebACL</code> (see <a>UpdateWebACL</a>), and delete a <code>WebACL</code> from AWS WAF (see <a>DeleteWebACL</a>).</p> <p> <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>"""
    name: "aws_sdk_waf_regional.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>WebACL</a>. You can't change the name of a <code>WebACL</code> after you create it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLSummary) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebACLSummary:
    out: WebACLSummary = {}  # type: ignore[typeddict-item]
    if "WebACLId" in data:
        out["web_acl_id"] = data["WebACLId"]
    else:
        raise DeserializationError("WebACLSummary.web_acl_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("WebACLSummary.name required")
    return out
