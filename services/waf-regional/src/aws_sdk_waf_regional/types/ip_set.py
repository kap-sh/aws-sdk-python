"""Generated from Smithy shape ``com.amazonaws.wafregional#IPSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.ip_set_descriptors
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.resource_name


class IPSet(TypedDict):
    ip_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>IPSetId</code> for an <code>IPSet</code>. You use <code>IPSetId</code> to get information about an <code>IPSet</code> (see <a>GetIPSet</a>), update an <code>IPSet</code> (see <a>UpdateIPSet</a>), insert an <code>IPSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete an <code>IPSet</code> from AWS WAF (see <a>DeleteIPSet</a>).</p> <p> <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>"""
    name: NotRequired["aws_sdk_waf_regional.types.resource_name.ResourceName"]
    """<p>A friendly name or description of the <a>IPSet</a>. You can't change the name of an <code>IPSet</code> after you create it.</p>"""
    ip_set_descriptors: "aws_sdk_waf_regional.types.ip_set_descriptors.IPSetDescriptors"
    """<p>The IP address type (<code>IPV4</code> or <code>IPV6</code>) and the IP address range (in CIDR notation) that web requests originate from. If the <code>WebACL</code> is associated with a CloudFront distribution and the viewer did not use an HTTP proxy or a load balancer to send the request, this is the value of the c-ip field in the CloudFront access logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSet) -> dict:
    out: dict = {}
    out["IPSetId"] = value["ip_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_waf_regional.types.ip_set_descriptors

    out["IPSetDescriptors"] = (
        aws_sdk_waf_regional.types.ip_set_descriptors.serialize_aws_json_1_1(
            value["ip_set_descriptors"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IPSet:
    out: IPSet = {}  # type: ignore[typeddict-item]
    if "IPSetId" in data:
        out["ip_set_id"] = data["IPSetId"]
    else:
        raise DeserializationError("IPSet.ip_set_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "IPSetDescriptors" in data:
        import aws_sdk_waf_regional.types.ip_set_descriptors

        out["ip_set_descriptors"] = (
            aws_sdk_waf_regional.types.ip_set_descriptors.deserialize_aws_json_1_1(
                data["IPSetDescriptors"]
            )
        )
    else:
        raise DeserializationError("IPSet.ip_set_descriptors required")
    return out
