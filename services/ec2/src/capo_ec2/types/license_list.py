"""Generated from Smithy shape ``com.amazonaws.ec2#LicenseList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.license_configuration

LicenseList: TypeAlias = list[
    "capo_ec2.types.license_configuration.LicenseConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LicenseList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.license_configuration

        capo_ec2.types.license_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LicenseList:
    import capo_ec2.types.license_configuration

    out: LicenseList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.license_configuration.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LicenseList:
    import capo_ec2.types.license_configuration

    out: LicenseList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.license_configuration.deserialize_ec2_query(child))
    return out
