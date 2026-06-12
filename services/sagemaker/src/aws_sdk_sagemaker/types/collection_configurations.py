"""Generated from Smithy shape ``com.amazonaws.sagemaker#CollectionConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.collection_configuration

CollectionConfigurations: TypeAlias = list[
    "aws_sdk_sagemaker.types.collection_configuration.CollectionConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectionConfigurations) -> list:
    import aws_sdk_sagemaker.types.collection_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.collection_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CollectionConfigurations:
    import aws_sdk_sagemaker.types.collection_configuration

    out: CollectionConfigurations = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.collection_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
