"""Generated from Smithy shape ``com.amazonaws.wafregional#IPSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.resource_name


class IPSetSummary(TypedDict, closed=True):
    ip_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>IPSetId</code> for an <a>IPSet</a>. You can use <code>IPSetId</code> in a <a>GetIPSet</a> request to get detailed information about an <a>IPSet</a>.</p>"""
    name: "capo_waf_regional.types.resource_name.ResourceName"
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
