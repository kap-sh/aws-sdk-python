"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRateBasedStatementManagedKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.scope


class GetRateBasedStatementManagedKeysRequest(TypedDict, closed=True):
    scope: "aws_sdk_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    web_acl_name: "aws_sdk_wafv2.types.entity_name.EntityName"
    """<p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>"""
    web_acl_id: "aws_sdk_wafv2.types.entity_id.EntityId"
    """<p>The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    rule_group_rule_name: NotRequired["aws_sdk_wafv2.types.entity_name.EntityName"]
    """<p>The name of the rule group reference statement in your web ACL. This is required only when you have the rate-based rule nested inside a rule group. </p>"""
    rule_name: "aws_sdk_wafv2.types.entity_name.EntityName"
    """<p>The name of the rate-based rule to get the keys for. If you have the rule defined inside a rule group that you're using in your web ACL, also provide the name of the rule group reference statement in the request parameter <code>RuleGroupRuleName</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedStatementManagedKeysRequest) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.scope

    out["Scope"] = aws_sdk_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    out["WebACLName"] = value["web_acl_name"]
    out["WebACLId"] = value["web_acl_id"]
    if "rule_group_rule_name" in value:
        out["RuleGroupRuleName"] = value["rule_group_rule_name"]
    out["RuleName"] = value["rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedStatementManagedKeysRequest:
    out: GetRateBasedStatementManagedKeysRequest = {}  # type: ignore[typeddict-item]
    if "Scope" in data:
        import aws_sdk_wafv2.types.scope

        out["scope"] = aws_sdk_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError(
            "GetRateBasedStatementManagedKeysRequest.scope required"
        )
    if "WebACLName" in data:
        out["web_acl_name"] = data["WebACLName"]
    else:
        raise DeserializationError(
            "GetRateBasedStatementManagedKeysRequest.web_acl_name required"
        )
    if "WebACLId" in data:
        out["web_acl_id"] = data["WebACLId"]
    else:
        raise DeserializationError(
            "GetRateBasedStatementManagedKeysRequest.web_acl_id required"
        )
    if "RuleGroupRuleName" in data:
        out["rule_group_rule_name"] = data["RuleGroupRuleName"]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError(
            "GetRateBasedStatementManagedKeysRequest.rule_name required"
        )
    return out
