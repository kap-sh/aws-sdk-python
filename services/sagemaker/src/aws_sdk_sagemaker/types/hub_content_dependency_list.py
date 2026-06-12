"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentDependencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_content_dependency

HubContentDependencyList: TypeAlias = list[
    "aws_sdk_sagemaker.types.hub_content_dependency.HubContentDependency"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentDependencyList) -> list:
    import aws_sdk_sagemaker.types.hub_content_dependency

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.hub_content_dependency.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HubContentDependencyList:
    import aws_sdk_sagemaker.types.hub_content_dependency

    out: HubContentDependencyList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.hub_content_dependency.deserialize_aws_json_1_1(
                item
            )
        )
    return out
