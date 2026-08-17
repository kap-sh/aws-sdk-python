"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_encryption_control

VpcEncryptionControlList: TypeAlias = list[
    "capo_ec2.types.vpc_encryption_control.VpcEncryptionControl"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionControlList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpc_encryption_control

        capo_ec2.types.vpc_encryption_control.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VpcEncryptionControlList:
    import capo_ec2.types.vpc_encryption_control

    out: VpcEncryptionControlList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.vpc_encryption_control.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VpcEncryptionControlList:
    import capo_ec2.types.vpc_encryption_control

    out: VpcEncryptionControlList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpc_encryption_control.deserialize_ec2_query(child))
    return out
