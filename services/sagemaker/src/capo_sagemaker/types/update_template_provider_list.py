"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTemplateProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.update_template_provider

UpdateTemplateProviderList: TypeAlias = list[
    "capo_sagemaker.types.update_template_provider.UpdateTemplateProvider"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTemplateProviderList) -> list:
    import capo_sagemaker.types.update_template_provider

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.update_template_provider.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateTemplateProviderList:
    import capo_sagemaker.types.update_template_provider

    out: UpdateTemplateProviderList = []
    for item in data:
        out.append(
            capo_sagemaker.types.update_template_provider.deserialize_aws_json_1_1(item)
        )
    return out
