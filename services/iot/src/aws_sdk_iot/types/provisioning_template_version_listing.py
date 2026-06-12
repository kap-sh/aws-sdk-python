"""Generated from Smithy shape ``com.amazonaws.iot#ProvisioningTemplateVersionListing``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.provisioning_template_version_summary

ProvisioningTemplateVersionListing: TypeAlias = list[
    "aws_sdk_iot.types.provisioning_template_version_summary.ProvisioningTemplateVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningTemplateVersionListing) -> list:
    import aws_sdk_iot.types.provisioning_template_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot.types.provisioning_template_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProvisioningTemplateVersionListing:
    import aws_sdk_iot.types.provisioning_template_version_summary

    out: ProvisioningTemplateVersionListing = []
    for item in data:
        out.append(
            aws_sdk_iot.types.provisioning_template_version_summary.deserialize_json(
                item
            )
        )
    return out
