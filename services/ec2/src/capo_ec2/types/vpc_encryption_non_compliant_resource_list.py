"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionNonCompliantResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_encryption_non_compliant_resource

VpcEncryptionNonCompliantResourceList: TypeAlias = list[
    "capo_ec2.types.vpc_encryption_non_compliant_resource.VpcEncryptionNonCompliantResource"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionNonCompliantResourceList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpc_encryption_non_compliant_resource

        capo_ec2.types.vpc_encryption_non_compliant_resource.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VpcEncryptionNonCompliantResourceList:
    import capo_ec2.types.vpc_encryption_non_compliant_resource

    out: VpcEncryptionNonCompliantResourceList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.vpc_encryption_non_compliant_resource.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> VpcEncryptionNonCompliantResourceList:
    import capo_ec2.types.vpc_encryption_non_compliant_resource

    out: VpcEncryptionNonCompliantResourceList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.vpc_encryption_non_compliant_resource.deserialize_ec2_query(
                child
            )
        )
    return out
