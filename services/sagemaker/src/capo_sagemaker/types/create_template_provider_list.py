"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTemplateProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.create_template_provider

CreateTemplateProviderList: TypeAlias = list[
    "capo_sagemaker.types.create_template_provider.CreateTemplateProvider"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTemplateProviderList) -> list:
    import capo_sagemaker.types.create_template_provider

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.create_template_provider.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreateTemplateProviderList:
    import capo_sagemaker.types.create_template_provider

    out: CreateTemplateProviderList = []
    for item in data:
        out.append(
            capo_sagemaker.types.create_template_provider.deserialize_aws_json_1_1(item)
        )
    return out
