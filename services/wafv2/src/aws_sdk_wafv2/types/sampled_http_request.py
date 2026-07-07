"""Generated from Smithy shape ``com.amazonaws.wafv2#SampledHTTPRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.action
    import aws_sdk_wafv2.types.captcha_response
    import aws_sdk_wafv2.types.challenge_response
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.http_headers
    import aws_sdk_wafv2.types.http_request
    import aws_sdk_wafv2.types.labels
    import aws_sdk_wafv2.types.response_status_code
    import aws_sdk_wafv2.types.sample_weight
    import aws_sdk_wafv2.types.timestamp


class SampledHTTPRequest(TypedDict, closed=True):
    request: "aws_sdk_wafv2.types.http_request.HTTPRequest"
    """<p>A complex type that contains detailed information about the request.</p>"""
    weight: "aws_sdk_wafv2.types.sample_weight.SampleWeight"
    """<p>A value that indicates how one result in the response relates proportionally to other results in the response. For example, a result that has a weight of <code>2</code> represents roughly twice as many web requests as a result that has a weight of <code>1</code>.</p>"""
    timestamp: NotRequired["aws_sdk_wafv2.types.timestamp.Timestamp"]
    """<p>The time at which WAF received the request from your Amazon Web Services resource, in Unix time format (in seconds).</p>"""
    action: NotRequired["aws_sdk_wafv2.types.action.Action"]
    """<p>The action that WAF applied to the request.</p>"""
    rule_name_within_rule_group: NotRequired[
        "aws_sdk_wafv2.types.entity_name.EntityName"
    ]
    """<p>The name of the <code>Rule</code> that the request matched. For managed rule groups, the format for this name is <code><vendor name>#<managed rule group name>#<rule name></code>. For your own rule groups, the format for this name is <code><rule group name>#<rule name></code>. If the rule is not in a rule group, this field is absent. </p>"""
    request_headers_inserted: NotRequired[
        "aws_sdk_wafv2.types.http_headers.HTTPHeaders"
    ]
    """<p>Custom request headers inserted by WAF into the request, according to the custom request configuration for the matching rule action.</p>"""
    response_code_sent: NotRequired[
        "aws_sdk_wafv2.types.response_status_code.ResponseStatusCode"
    ]
    """<p>The response code that was sent for the request.</p>"""
    labels: NotRequired["aws_sdk_wafv2.types.labels.Labels"]
    """<p>Labels applied to the web request by matching rules. WAF applies fully qualified labels to matching web requests. A fully qualified label is the concatenation of a label namespace and a rule label. The rule's rule group or web ACL defines the label namespace. </p> <p>For example, <code>awswaf:111122223333:myRuleGroup:testRules:testNS1:testNS2:labelNameA</code> or <code>awswaf:managed:aws:managed-rule-set:header:encoding:utf8</code>. </p>"""
    captcha_response: NotRequired[
        "aws_sdk_wafv2.types.captcha_response.CaptchaResponse"
    ]
    """<p>The <code>CAPTCHA</code> response for the request.</p>"""
    challenge_response: NotRequired[
        "aws_sdk_wafv2.types.challenge_response.ChallengeResponse"
    ]
    """<p>The <code>Challenge</code> response for the request.</p>"""
    overridden_action: NotRequired["aws_sdk_wafv2.types.action.Action"]
    """<p>Used only for rule group rules that have a rule action override in place in the web ACL. This is the action that the rule group rule is configured for, and not the action that was applied to the request. The action that WAF applied is the <code>Action</code> value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SampledHTTPRequest) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.http_request

    out["Request"] = aws_sdk_wafv2.types.http_request.serialize_aws_json_1_1(
        value["request"]
    )
    out["Weight"] = value.get("weight", 0)
    if "timestamp" in value:
        import aws_sdk_wafv2.types.timestamp

        out["Timestamp"] = aws_sdk_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "action" in value:
        out["Action"] = value["action"]
    if "rule_name_within_rule_group" in value:
        out["RuleNameWithinRuleGroup"] = value["rule_name_within_rule_group"]
    if "request_headers_inserted" in value:
        import aws_sdk_wafv2.types.http_headers

        out["RequestHeadersInserted"] = (
            aws_sdk_wafv2.types.http_headers.serialize_aws_json_1_1(
                value["request_headers_inserted"]
            )
        )
    if "response_code_sent" in value:
        out["ResponseCodeSent"] = value["response_code_sent"]
    if "labels" in value:
        import aws_sdk_wafv2.types.labels

        out["Labels"] = aws_sdk_wafv2.types.labels.serialize_aws_json_1_1(
            value["labels"]
        )
    if "captcha_response" in value:
        import aws_sdk_wafv2.types.captcha_response

        out["CaptchaResponse"] = (
            aws_sdk_wafv2.types.captcha_response.serialize_aws_json_1_1(
                value["captcha_response"]
            )
        )
    if "challenge_response" in value:
        import aws_sdk_wafv2.types.challenge_response

        out["ChallengeResponse"] = (
            aws_sdk_wafv2.types.challenge_response.serialize_aws_json_1_1(
                value["challenge_response"]
            )
        )
    if "overridden_action" in value:
        out["OverriddenAction"] = value["overridden_action"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SampledHTTPRequest:
    out: SampledHTTPRequest = {}  # type: ignore[typeddict-item]
    if "Request" in data:
        import aws_sdk_wafv2.types.http_request

        out["request"] = aws_sdk_wafv2.types.http_request.deserialize_aws_json_1_1(
            data["Request"]
        )
    else:
        raise DeserializationError("SampledHTTPRequest.request required")
    if "Weight" in data:
        out["weight"] = data["Weight"]
    else:
        out["weight"] = 0
    if "Timestamp" in data:
        import aws_sdk_wafv2.types.timestamp

        out["timestamp"] = aws_sdk_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    if "Action" in data:
        out["action"] = data["Action"]
    if "RuleNameWithinRuleGroup" in data:
        out["rule_name_within_rule_group"] = data["RuleNameWithinRuleGroup"]
    if "RequestHeadersInserted" in data:
        import aws_sdk_wafv2.types.http_headers

        out["request_headers_inserted"] = (
            aws_sdk_wafv2.types.http_headers.deserialize_aws_json_1_1(
                data["RequestHeadersInserted"]
            )
        )
    if "ResponseCodeSent" in data:
        out["response_code_sent"] = data["ResponseCodeSent"]
    if "Labels" in data:
        import aws_sdk_wafv2.types.labels

        out["labels"] = aws_sdk_wafv2.types.labels.deserialize_aws_json_1_1(
            data["Labels"]
        )
    if "CaptchaResponse" in data:
        import aws_sdk_wafv2.types.captcha_response

        out["captcha_response"] = (
            aws_sdk_wafv2.types.captcha_response.deserialize_aws_json_1_1(
                data["CaptchaResponse"]
            )
        )
    if "ChallengeResponse" in data:
        import aws_sdk_wafv2.types.challenge_response

        out["challenge_response"] = (
            aws_sdk_wafv2.types.challenge_response.deserialize_aws_json_1_1(
                data["ChallengeResponse"]
            )
        )
    if "OverriddenAction" in data:
        out["overridden_action"] = data["OverriddenAction"]
    return out
