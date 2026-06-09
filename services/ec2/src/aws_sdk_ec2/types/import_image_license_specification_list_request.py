"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageLicenseSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_license_configuration_request

ImportImageLicenseSpecificationListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.import_image_license_configuration_request.ImportImageLicenseConfigurationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportImageLicenseSpecificationListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.import_image_license_configuration_request

        aws_sdk_ec2.types.import_image_license_configuration_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> ImportImageLicenseSpecificationListRequest:
    import aws_sdk_ec2.types.import_image_license_configuration_request

    out: ImportImageLicenseSpecificationListRequest = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.import_image_license_configuration_request.deserialize_ec2_query(
                child
            )
        )
    return out
