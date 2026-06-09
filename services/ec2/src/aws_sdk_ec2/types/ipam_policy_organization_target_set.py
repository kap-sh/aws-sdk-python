"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyOrganizationTargetSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_organization_target

IpamPolicyOrganizationTargetSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_policy_organization_target.IpamPolicyOrganizationTarget"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyOrganizationTargetSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_policy_organization_target

        aws_sdk_ec2.types.ipam_policy_organization_target.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPolicyOrganizationTargetSet:
    import aws_sdk_ec2.types.ipam_policy_organization_target

    out: IpamPolicyOrganizationTargetSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.ipam_policy_organization_target.deserialize_ec2_query(
                child
            )
        )
    return out
