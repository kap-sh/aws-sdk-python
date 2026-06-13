"""Generated from Smithy shape ``com.amazonaws.launchwizard#SpecificationsConditionalData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_conditional_field

SpecificationsConditionalData: TypeAlias = list[
    "aws_sdk_launch_wizard.types.deployment_conditional_field.DeploymentConditionalField"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpecificationsConditionalData) -> list:
    import aws_sdk_launch_wizard.types.deployment_conditional_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_launch_wizard.types.deployment_conditional_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SpecificationsConditionalData:
    import aws_sdk_launch_wizard.types.deployment_conditional_field

    out: SpecificationsConditionalData = []
    for item in data:
        out.append(
            aws_sdk_launch_wizard.types.deployment_conditional_field.deserialize_json(
                item
            )
        )
    return out
