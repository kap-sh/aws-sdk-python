"""Generated from Smithy shape ``com.amazonaws.ec2#LicenseSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.license_configuration_request

LicenseSpecificationListRequest: TypeAlias = list[
    "capo_ec2.types.license_configuration_request.LicenseConfigurationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LicenseSpecificationListRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.license_configuration_request

        capo_ec2.types.license_configuration_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> LicenseSpecificationListRequest:
    import capo_ec2.types.license_configuration_request

    out: LicenseSpecificationListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.license_configuration_request.deserialize_ec2_query(child)
        )
    return out
