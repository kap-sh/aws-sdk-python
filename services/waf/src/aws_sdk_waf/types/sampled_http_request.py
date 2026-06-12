"""Generated from Smithy shape ``com.amazonaws.waf#SampledHTTPRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.action
    import aws_sdk_waf.types.http_request
    import aws_sdk_waf.types.resource_id
    import aws_sdk_waf.types.sample_weight
    import aws_sdk_waf.types.timestamp


class SampledHTTPRequest(TypedDict):
    request: "aws_sdk_waf.types.http_request.HTTPRequest"
    """<p>A complex type that contains detailed information about the request.</p>"""
    weight: "aws_sdk_waf.types.sample_weight.SampleWeight"
    """<p>A value that indicates how one result in the response relates proportionally to other results in the response. A result that has a weight of <code>2</code> represents roughly twice as many CloudFront web requests as a result that has a weight of <code>1</code>.</p>"""
    timestamp: NotRequired["aws_sdk_waf.types.timestamp.Timestamp"]
    """<p>The time at which AWS WAF received the request from your AWS resource, in Unix time format (in seconds).</p>"""
    action: NotRequired["aws_sdk_waf.types.action.Action"]
    """<p>The action for the <code>Rule</code> that the request matched: <code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>.</p>"""
    rule_within_rule_group: NotRequired["aws_sdk_waf.types.resource_id.ResourceId"]
    """<p>This value is returned if the <code>GetSampledRequests</code> request specifies the ID of a <code>RuleGroup</code> rather than the ID of an individual rule. <code>RuleWithinRuleGroup</code> is the rule within the specified <code>RuleGroup</code> that matched the request listed in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SampledHTTPRequest) -> dict:
    out: dict = {}
    import aws_sdk_waf.types.http_request

    out["Request"] = aws_sdk_waf.types.http_request.serialize_aws_json_1_1(
        value["request"]
    )
    out["Weight"] = value.get("weight", 0)
    if "timestamp" in value:
        import aws_sdk_waf.types.timestamp

        out["Timestamp"] = aws_sdk_waf.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "action" in value:
        out["Action"] = value["action"]
    if "rule_within_rule_group" in value:
        out["RuleWithinRuleGroup"] = value["rule_within_rule_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SampledHTTPRequest:
    out: SampledHTTPRequest = {}  # type: ignore[typeddict-item]
    if "Request" in data:
        import aws_sdk_waf.types.http_request

        out["request"] = aws_sdk_waf.types.http_request.deserialize_aws_json_1_1(
            data["Request"]
        )
    else:
        raise DeserializationError("SampledHTTPRequest.request required")
    if "Weight" in data:
        out["weight"] = data["Weight"]
    else:
        out["weight"] = 0
    if "Timestamp" in data:
        import aws_sdk_waf.types.timestamp

        out["timestamp"] = aws_sdk_waf.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    if "Action" in data:
        out["action"] = data["Action"]
    if "RuleWithinRuleGroup" in data:
        out["rule_within_rule_group"] = data["RuleWithinRuleGroup"]
    return out
