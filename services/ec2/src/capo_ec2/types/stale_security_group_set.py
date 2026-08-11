"""Generated from Smithy shape ``com.amazonaws.ec2#StaleSecurityGroupSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.stale_security_group

StaleSecurityGroupSet: TypeAlias = list[
    "capo_ec2.types.stale_security_group.StaleSecurityGroup"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StaleSecurityGroupSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.stale_security_group

        capo_ec2.types.stale_security_group.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> StaleSecurityGroupSet:
    import capo_ec2.types.stale_security_group

    out: StaleSecurityGroupSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.stale_security_group.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> StaleSecurityGroupSet:
    import capo_ec2.types.stale_security_group

    out: StaleSecurityGroupSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.stale_security_group.deserialize_ec2_query(child))
    return out
