"""Generated from Smithy shape ``com.amazonaws.ec2#AllowedPrincipalSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allowed_principal

AllowedPrincipalSet: TypeAlias = list[
    "capo_ec2.types.allowed_principal.AllowedPrincipal"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllowedPrincipalSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.allowed_principal

        capo_ec2.types.allowed_principal.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AllowedPrincipalSet:
    import capo_ec2.types.allowed_principal

    out: AllowedPrincipalSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.allowed_principal.deserialize_ec2_query(child))
    return out
