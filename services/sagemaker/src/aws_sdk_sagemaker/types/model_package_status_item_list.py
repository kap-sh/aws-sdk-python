"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageStatusItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_status_item

ModelPackageStatusItemList: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_package_status_item.ModelPackageStatusItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageStatusItemList) -> list:
    import aws_sdk_sagemaker.types.model_package_status_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_package_status_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelPackageStatusItemList:
    import aws_sdk_sagemaker.types.model_package_status_item

    out: ModelPackageStatusItemList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_package_status_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
