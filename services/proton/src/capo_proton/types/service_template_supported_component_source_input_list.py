"""Generated from Smithy shape ``com.amazonaws.proton#ServiceTemplateSupportedComponentSourceInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.service_template_supported_component_source_type

ServiceTemplateSupportedComponentSourceInputList: TypeAlias = list[
    "capo_proton.types.service_template_supported_component_source_type.ServiceTemplateSupportedComponentSourceType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ServiceTemplateSupportedComponentSourceInputList,
) -> list:
    return list(value)


def deserialize_aws_json_1_0(
    data: list,
) -> ServiceTemplateSupportedComponentSourceInputList:
    return list(data)
