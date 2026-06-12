"""Generated from Smithy shape ``com.amazonaws.iot#ProvisioningTemplateListing``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.provisioning_template_summary

ProvisioningTemplateListing: TypeAlias = list[
    "aws_sdk_iot.types.provisioning_template_summary.ProvisioningTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningTemplateListing) -> list:
    import aws_sdk_iot.types.provisioning_template_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.provisioning_template_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProvisioningTemplateListing:
    import aws_sdk_iot.types.provisioning_template_summary

    out: ProvisioningTemplateListing = []
    for item in data:
        out.append(
            aws_sdk_iot.types.provisioning_template_summary.deserialize_json(item)
        )
    return out
