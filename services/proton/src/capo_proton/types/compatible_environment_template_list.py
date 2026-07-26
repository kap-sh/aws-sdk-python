"""Generated from Smithy shape ``com.amazonaws.proton#CompatibleEnvironmentTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.compatible_environment_template

CompatibleEnvironmentTemplateList: TypeAlias = list[
    "capo_proton.types.compatible_environment_template.CompatibleEnvironmentTemplate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompatibleEnvironmentTemplateList) -> list:
    import capo_proton.types.compatible_environment_template

    out: list = []
    for item in value:
        out.append(
            capo_proton.types.compatible_environment_template.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CompatibleEnvironmentTemplateList:
    import capo_proton.types.compatible_environment_template

    out: CompatibleEnvironmentTemplateList = []
    for item in data:
        out.append(
            capo_proton.types.compatible_environment_template.deserialize_aws_json_1_0(
                item
            )
        )
    return out
