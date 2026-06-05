"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SecurityGroupRuleDescription(TypedDict):
    security_group_rule_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group rule.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the security group rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRuleDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "security_group_rule_id" in value:
        pairs.append(
            (f"{prefix}.SecurityGroupRuleId", str(value["security_group_rule_id"]))
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_ec2_query(el: Element) -> SecurityGroupRuleDescription:
    out: SecurityGroupRuleDescription = {}  # type: ignore[typeddict-item]
    child_security_group_rule_id = el.find("SecurityGroupRuleId")
    if child_security_group_rule_id is not None:
        out["security_group_rule_id"] = str(child_security_group_rule_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
