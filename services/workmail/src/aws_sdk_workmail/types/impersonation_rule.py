"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.access_effect
    import aws_sdk_workmail.types.impersonation_rule_description
    import aws_sdk_workmail.types.impersonation_rule_id
    import aws_sdk_workmail.types.impersonation_rule_name
    import aws_sdk_workmail.types.target_users


class ImpersonationRule(TypedDict):
    impersonation_rule_id: (
        "aws_sdk_workmail.types.impersonation_rule_id.ImpersonationRuleId"
    )
    """<p>The identifier of the rule.</p>"""
    name: NotRequired[
        "aws_sdk_workmail.types.impersonation_rule_name.ImpersonationRuleName"
    ]
    """<p>The rule name.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.impersonation_rule_description.ImpersonationRuleDescription"
    ]
    """<p>The rule description.</p>"""
    effect: "aws_sdk_workmail.types.access_effect.AccessEffect"
    """<p>The effect of the rule when it matches the input. Allowed effect values are <code>ALLOW</code> or <code>DENY</code>.</p>"""
    target_users: NotRequired["aws_sdk_workmail.types.target_users.TargetUsers"]
    """<p>A list of user IDs that match the rule.</p>"""
    not_target_users: NotRequired["aws_sdk_workmail.types.target_users.TargetUsers"]
    """<p>A list of user IDs that don't match the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRule) -> dict:
    out: dict = {}
    out["ImpersonationRuleId"] = value["impersonation_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_workmail.types.access_effect

    out["Effect"] = aws_sdk_workmail.types.access_effect.serialize_aws_json_1_1(
        value["effect"]
    )
    if "target_users" in value:
        import aws_sdk_workmail.types.target_users

        out["TargetUsers"] = aws_sdk_workmail.types.target_users.serialize_aws_json_1_1(
            value["target_users"]
        )
    if "not_target_users" in value:
        import aws_sdk_workmail.types.target_users

        out["NotTargetUsers"] = (
            aws_sdk_workmail.types.target_users.serialize_aws_json_1_1(
                value["not_target_users"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImpersonationRule:
    out: ImpersonationRule = {}  # type: ignore[typeddict-item]
    if "ImpersonationRuleId" in data:
        out["impersonation_rule_id"] = data["ImpersonationRuleId"]
    else:
        raise DeserializationError("ImpersonationRule.impersonation_rule_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Effect" in data:
        import aws_sdk_workmail.types.access_effect

        out["effect"] = aws_sdk_workmail.types.access_effect.deserialize_aws_json_1_1(
            data["Effect"]
        )
    else:
        raise DeserializationError("ImpersonationRule.effect required")
    if "TargetUsers" in data:
        import aws_sdk_workmail.types.target_users

        out["target_users"] = (
            aws_sdk_workmail.types.target_users.deserialize_aws_json_1_1(
                data["TargetUsers"]
            )
        )
    if "NotTargetUsers" in data:
        import aws_sdk_workmail.types.target_users

        out["not_target_users"] = (
            aws_sdk_workmail.types.target_users.deserialize_aws_json_1_1(
                data["NotTargetUsers"]
            )
        )
    return out
