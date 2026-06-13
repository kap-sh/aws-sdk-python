"""Generated from Smithy shape ``com.amazonaws.proton#CompatibleEnvironmentTemplateInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.compatible_environment_template_input

CompatibleEnvironmentTemplateInputList: TypeAlias = list[
    "aws_sdk_proton.types.compatible_environment_template_input.CompatibleEnvironmentTemplateInput"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompatibleEnvironmentTemplateInputList) -> list:
    import aws_sdk_proton.types.compatible_environment_template_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.compatible_environment_template_input.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CompatibleEnvironmentTemplateInputList:
    import aws_sdk_proton.types.compatible_environment_template_input

    out: CompatibleEnvironmentTemplateInputList = []
    for item in data:
        out.append(
            aws_sdk_proton.types.compatible_environment_template_input.deserialize_aws_json_1_0(
                item
            )
        )
    return out
