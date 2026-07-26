"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyDocumentSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_document

IpamPolicyDocumentSet: TypeAlias = list[
    "capo_ec2.types.ipam_policy_document.IpamPolicyDocument"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyDocumentSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_policy_document

        capo_ec2.types.ipam_policy_document.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPolicyDocumentSet:
    import capo_ec2.types.ipam_policy_document

    out: IpamPolicyDocumentSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_policy_document.deserialize_ec2_query(child))
    return out
