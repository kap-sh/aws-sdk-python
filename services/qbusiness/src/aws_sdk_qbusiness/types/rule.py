"""Generated from Smithy shape ``com.amazonaws.qbusiness#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.rule_configuration
    import aws_sdk_qbusiness.types.rule_type
    import aws_sdk_qbusiness.types.users_and_groups


class Rule(TypedDict, closed=True):
    included_users_and_groups: NotRequired[
        "aws_sdk_qbusiness.types.users_and_groups.UsersAndGroups"
    ]
    """<p>Users and groups to be included in a rule.</p>"""
    excluded_users_and_groups: NotRequired[
        "aws_sdk_qbusiness.types.users_and_groups.UsersAndGroups"
    ]
    """<p>Users and groups to be excluded from a rule.</p>"""
    rule_type: "aws_sdk_qbusiness.types.rule_type.RuleType"
    """<p>The type of rule.</p>"""
    rule_configuration: NotRequired[
        "aws_sdk_qbusiness.types.rule_configuration.RuleConfiguration"
    ]
    """<p>The configuration information for a rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    if "included_users_and_groups" in value:
        import aws_sdk_qbusiness.types.users_and_groups

        out["includedUsersAndGroups"] = (
            aws_sdk_qbusiness.types.users_and_groups.serialize_json(
                value["included_users_and_groups"]
            )
        )
    if "excluded_users_and_groups" in value:
        import aws_sdk_qbusiness.types.users_and_groups

        out["excludedUsersAndGroups"] = (
            aws_sdk_qbusiness.types.users_and_groups.serialize_json(
                value["excluded_users_and_groups"]
            )
        )
    import aws_sdk_qbusiness.types.rule_type

    out["ruleType"] = aws_sdk_qbusiness.types.rule_type.serialize_json(
        value["rule_type"]
    )
    if "rule_configuration" in value:
        import aws_sdk_qbusiness.types.rule_configuration

        out["ruleConfiguration"] = (
            aws_sdk_qbusiness.types.rule_configuration.serialize_json(
                value["rule_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "includedUsersAndGroups" in data:
        import aws_sdk_qbusiness.types.users_and_groups

        out["included_users_and_groups"] = (
            aws_sdk_qbusiness.types.users_and_groups.deserialize_json(
                data["includedUsersAndGroups"]
            )
        )
    if "excludedUsersAndGroups" in data:
        import aws_sdk_qbusiness.types.users_and_groups

        out["excluded_users_and_groups"] = (
            aws_sdk_qbusiness.types.users_and_groups.deserialize_json(
                data["excludedUsersAndGroups"]
            )
        )
    if "ruleType" in data:
        import aws_sdk_qbusiness.types.rule_type

        out["rule_type"] = aws_sdk_qbusiness.types.rule_type.deserialize_json(
            data["ruleType"]
        )
    else:
        raise DeserializationError("Rule.rule_type required")
    if "ruleConfiguration" in data:
        import aws_sdk_qbusiness.types.rule_configuration

        out["rule_configuration"] = (
            aws_sdk_qbusiness.types.rule_configuration.deserialize_json(
                data["ruleConfiguration"]
            )
        )
    return out
