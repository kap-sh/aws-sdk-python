"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageLicenseSpecificationListResponse``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_license_configuration_response

ImportImageLicenseSpecificationListResponse: TypeAlias = list[
    "aws_sdk_ec2.types.import_image_license_configuration_response.ImportImageLicenseConfigurationResponse"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportImageLicenseSpecificationListResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.import_image_license_configuration_response

        aws_sdk_ec2.types.import_image_license_configuration_response.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> ImportImageLicenseSpecificationListResponse:
    import aws_sdk_ec2.types.import_image_license_configuration_response

    out: ImportImageLicenseSpecificationListResponse = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.import_image_license_configuration_response.deserialize_ec2_query(
                child
            )
        )
    return out
