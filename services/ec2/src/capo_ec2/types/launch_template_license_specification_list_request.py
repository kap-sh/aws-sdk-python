"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateLicenseSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_license_configuration_request

LaunchTemplateLicenseSpecificationListRequest: TypeAlias = list[
    "capo_ec2.types.launch_template_license_configuration_request.LaunchTemplateLicenseConfigurationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateLicenseSpecificationListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_template_license_configuration_request

        capo_ec2.types.launch_template_license_configuration_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateLicenseSpecificationListRequest:
    import capo_ec2.types.launch_template_license_configuration_request

    out: LaunchTemplateLicenseSpecificationListRequest = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.launch_template_license_configuration_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LaunchTemplateLicenseSpecificationListRequest:
    import capo_ec2.types.launch_template_license_configuration_request

    out: LaunchTemplateLicenseSpecificationListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.launch_template_license_configuration_request.deserialize_ec2_query(
                child
            )
        )
    return out
