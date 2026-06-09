"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_rule_id
    import aws_sdk_ec2.types.security_group_rule_request


class SecurityGroupRuleUpdate(TypedDict):
    security_group_rule_id: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_id.SecurityGroupRuleId"
    ]
    """<p>The ID of the security group rule.</p>"""
    security_group_rule: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_request.SecurityGroupRuleRequest"
    ]
    """<p>Information about the security group rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRuleUpdate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "security_group_rule_id" in value:
        pairs.append(
            (f"{prefix}.SecurityGroupRuleId", str(value["security_group_rule_id"]))
        )
    if "security_group_rule" in value:
        import aws_sdk_ec2.types.security_group_rule_request

        aws_sdk_ec2.types.security_group_rule_request.serialize_ec2_query(
            value["security_group_rule"], pairs, f"{prefix}.SecurityGroupRule"
        )


def deserialize_ec2_query(el: Element) -> SecurityGroupRuleUpdate:
    out: SecurityGroupRuleUpdate = {}  # type: ignore[typeddict-item]
    child_security_group_rule_id = el.find("SecurityGroupRuleId")
    if child_security_group_rule_id is not None:
        out["security_group_rule_id"] = str(child_security_group_rule_id.text or "")
    child_security_group_rule = el.find("SecurityGroupRule")
    if child_security_group_rule is not None:
        import aws_sdk_ec2.types.security_group_rule_request

        out["security_group_rule"] = (
            aws_sdk_ec2.types.security_group_rule_request.deserialize_ec2_query(
                child_security_group_rule
            )
        )
    return out
