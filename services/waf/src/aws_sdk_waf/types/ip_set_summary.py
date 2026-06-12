"""Generated from Smithy shape ``com.amazonaws.waf#IPSetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.resource_id
    import aws_sdk_waf.types.resource_name


class IPSetSummary(TypedDict):
    ip_set_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>IPSetId</code> for an <a>IPSet</a>. You can use <code>IPSetId</code> in a <a>GetIPSet</a> request to get detailed information about an <a>IPSet</a>.</p>"""
    name: "aws_sdk_waf.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>IPSet</a>. You can't change the name of an <code>IPSet</code> after you create it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetSummary) -> dict:
    out: dict = {}
    out["IPSetId"] = value["ip_set_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IPSetSummary:
    out: IPSetSummary = {}  # type: ignore[typeddict-item]
    if "IPSetId" in data:
        out["ip_set_id"] = data["IPSetId"]
    else:
        raise DeserializationError("IPSetSummary.ip_set_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("IPSetSummary.name required")
    return out
