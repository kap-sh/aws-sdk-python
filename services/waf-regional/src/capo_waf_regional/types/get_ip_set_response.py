"""Generated from Smithy shape ``com.amazonaws.wafregional#GetIPSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.ip_set


class GetIPSetResponse(TypedDict, closed=True):
    ip_set: NotRequired["capo_waf_regional.types.ip_set.IPSet"]
    """<p>Information about the <a>IPSet</a> that you specified in the <code>GetIPSet</code> request. For more information, see the following topics:</p> <ul> <li> <p> <a>IPSet</a>: Contains <code>IPSetDescriptors</code>, <code>IPSetId</code>, and <code>Name</code> </p> </li> <li> <p> <code>IPSetDescriptors</code>: Contains an array of <a>IPSetDescriptor</a> objects. Each <code>IPSetDescriptor</code> object contains <code>Type</code> and <code>Value</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIPSetResponse) -> dict:
    out: dict = {}
    if "ip_set" in value:
        import capo_waf_regional.types.ip_set

        out["IPSet"] = capo_waf_regional.types.ip_set.serialize_aws_json_1_1(
            value["ip_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIPSetResponse:
    out: GetIPSetResponse = {}  # type: ignore[typeddict-item]
    if "IPSet" in data:
        import capo_waf_regional.types.ip_set

        out["ip_set"] = capo_waf_regional.types.ip_set.deserialize_aws_json_1_1(
            data["IPSet"]
        )
    return out
