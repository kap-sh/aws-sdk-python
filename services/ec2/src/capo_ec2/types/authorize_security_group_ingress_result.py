"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeSecurityGroupIngressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.security_group_rule_list

AuthorizeSecurityGroupIngressResult = TypedDict(
    "AuthorizeSecurityGroupIngressResult",
    {
        "return": NotRequired["capo_ec2.types.boolean.Boolean"],
        "security_group_rules": NotRequired[
            "capo_ec2.types.security_group_rule_list.SecurityGroupRuleList"
        ],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AuthorizeSecurityGroupIngressResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "return" in value:
        pairs.append((f"{prefix}.Return", "true" if value["return"] else "false"))
    if "security_group_rules" in value:
        import capo_ec2.types.security_group_rule_list

        capo_ec2.types.security_group_rule_list.serialize_ec2_query(
            value["security_group_rules"], pairs, f"{prefix}.SecurityGroupRuleSet"
        )


def deserialize_ec2_query(el: Element) -> AuthorizeSecurityGroupIngressResult:
    out: AuthorizeSecurityGroupIngressResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    if el.find("SecurityGroupRuleSet") is not None:
        import capo_ec2.types.security_group_rule_list

        out["security_group_rules"] = (
            capo_ec2.types.security_group_rule_list.deserialize_ec2_query(
                el, "SecurityGroupRuleSet"
            )
        )
    return out
