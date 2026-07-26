"""Generated from Smithy shape ``com.amazonaws.wafregional#GetWebACLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.web_acl


class GetWebACLResponse(TypedDict, closed=True):
    web_acl: NotRequired["capo_waf_regional.types.web_acl.WebACL"]
    """<p>Information about the <a>WebACL</a> that you specified in the <code>GetWebACL</code> request. For more information, see the following topics:</p> <ul> <li> <p> <a>WebACL</a>: Contains <code>DefaultAction</code>, <code>MetricName</code>, <code>Name</code>, an array of <code>Rule</code> objects, and <code>WebACLId</code> </p> </li> <li> <p> <code>DefaultAction</code> (Data type is <a>WafAction</a>): Contains <code>Type</code> </p> </li> <li> <p> <code>Rules</code>: Contains an array of <code>ActivatedRule</code> objects, which contain <code>Action</code>, <code>Priority</code>, and <code>RuleId</code> </p> </li> <li> <p> <code>Action</code>: Contains <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWebACLResponse) -> dict:
    out: dict = {}
    if "web_acl" in value:
        import capo_waf_regional.types.web_acl

        out["WebACL"] = capo_waf_regional.types.web_acl.serialize_aws_json_1_1(
            value["web_acl"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWebACLResponse:
    out: GetWebACLResponse = {}  # type: ignore[typeddict-item]
    if "WebACL" in data:
        import capo_waf_regional.types.web_acl

        out["web_acl"] = capo_waf_regional.types.web_acl.deserialize_aws_json_1_1(
            data["WebACL"]
        )
    return out
