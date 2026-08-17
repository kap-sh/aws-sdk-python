"""Generated from Smithy shape ``com.amazonaws.ec2#PrincipalIdFormatList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.principal_id_format

PrincipalIdFormatList: TypeAlias = list[
    "capo_ec2.types.principal_id_format.PrincipalIdFormat"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrincipalIdFormatList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.principal_id_format

        capo_ec2.types.principal_id_format.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PrincipalIdFormatList:
    import capo_ec2.types.principal_id_format

    out: PrincipalIdFormatList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.principal_id_format.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PrincipalIdFormatList:
    import capo_ec2.types.principal_id_format

    out: PrincipalIdFormatList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.principal_id_format.deserialize_ec2_query(child))
    return out
