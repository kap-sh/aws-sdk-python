"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupReferencesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_references


class DescribeSecurityGroupReferencesResult(TypedDict, closed=True):
    security_group_reference_set: NotRequired[
        "capo_ec2.types.security_group_references.SecurityGroupReferences"
    ]
    """<p>Information about the VPCs with the referencing security groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecurityGroupReferencesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "security_group_reference_set" in value:
        import capo_ec2.types.security_group_references

        capo_ec2.types.security_group_references.serialize_ec2_query(
            value["security_group_reference_set"],
            pairs,
            f"{prefix}.SecurityGroupReferenceSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeSecurityGroupReferencesResult:
    out: DescribeSecurityGroupReferencesResult = {}  # type: ignore[typeddict-item]
    if el.find("SecurityGroupReferenceSet") is not None:
        import capo_ec2.types.security_group_references

        out["security_group_reference_set"] = (
            capo_ec2.types.security_group_references.deserialize_ec2_query(
                el, "SecurityGroupReferenceSet"
            )
        )
    return out
