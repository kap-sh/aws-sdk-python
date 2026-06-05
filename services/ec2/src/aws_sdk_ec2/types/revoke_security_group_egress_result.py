"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeSecurityGroupEgressResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.revoked_security_group_rule_list

RevokeSecurityGroupEgressResult = TypedDict(
    "RevokeSecurityGroupEgressResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "unknown_ip_permissions": NotRequired[
            "aws_sdk_ec2.types.ip_permission_list.IpPermissionList"
        ],
        "revoked_security_group_rules": NotRequired[
            "aws_sdk_ec2.types.revoked_security_group_rule_list.RevokedSecurityGroupRuleList"
        ],
    },
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RevokeSecurityGroupEgressResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "return" in value:
        pairs.append((f"{prefix}.Return", "true" if value["return"] else "false"))
    if "unknown_ip_permissions" in value:
        import aws_sdk_ec2.types.ip_permission_list

        aws_sdk_ec2.types.ip_permission_list.serialize_ec2_query(
            value["unknown_ip_permissions"], pairs, f"{prefix}.UnknownIpPermissionSet"
        )
    if "revoked_security_group_rules" in value:
        import aws_sdk_ec2.types.revoked_security_group_rule_list

        aws_sdk_ec2.types.revoked_security_group_rule_list.serialize_ec2_query(
            value["revoked_security_group_rules"],
            pairs,
            f"{prefix}.RevokedSecurityGroupRuleSet",
        )


def deserialize_ec2_query(el: Element) -> RevokeSecurityGroupEgressResult:
    out: RevokeSecurityGroupEgressResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    if el.find("UnknownIpPermissionSet") is not None:
        import aws_sdk_ec2.types.ip_permission_list

        out["unknown_ip_permissions"] = (
            aws_sdk_ec2.types.ip_permission_list.deserialize_ec2_query(
                el, "UnknownIpPermissionSet"
            )
        )
    if el.find("RevokedSecurityGroupRuleSet") is not None:
        import aws_sdk_ec2.types.revoked_security_group_rule_list

        out["revoked_security_group_rules"] = (
            aws_sdk_ec2.types.revoked_security_group_rule_list.deserialize_ec2_query(
                el, "RevokedSecurityGroupRuleSet"
            )
        )
    return out
