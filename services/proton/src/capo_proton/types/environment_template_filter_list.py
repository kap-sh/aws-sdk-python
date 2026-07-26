"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentTemplateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.environment_template_filter

EnvironmentTemplateFilterList: TypeAlias = list[
    "capo_proton.types.environment_template_filter.EnvironmentTemplateFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentTemplateFilterList) -> list:
    import capo_proton.types.environment_template_filter

    out: list = []
    for item in value:
        out.append(
            capo_proton.types.environment_template_filter.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EnvironmentTemplateFilterList:
    import capo_proton.types.environment_template_filter

    out: EnvironmentTemplateFilterList = []
    for item in data:
        out.append(
            capo_proton.types.environment_template_filter.deserialize_aws_json_1_0(item)
        )
    return out
