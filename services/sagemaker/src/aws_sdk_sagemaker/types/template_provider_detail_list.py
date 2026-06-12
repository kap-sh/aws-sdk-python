"""Generated from Smithy shape ``com.amazonaws.sagemaker#TemplateProviderDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.template_provider_detail

TemplateProviderDetailList: TypeAlias = list[
    "aws_sdk_sagemaker.types.template_provider_detail.TemplateProviderDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TemplateProviderDetailList) -> list:
    import aws_sdk_sagemaker.types.template_provider_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.template_provider_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TemplateProviderDetailList:
    import aws_sdk_sagemaker.types.template_provider_detail

    out: TemplateProviderDetailList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.template_provider_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
