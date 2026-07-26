"""Generated from Smithy shape ``com.amazonaws.sagemaker#CollectionConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.collection_configuration

CollectionConfigurations: TypeAlias = list[
    "capo_sagemaker.types.collection_configuration.CollectionConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectionConfigurations) -> list:
    import capo_sagemaker.types.collection_configuration

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.collection_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CollectionConfigurations:
    import capo_sagemaker.types.collection_configuration

    out: CollectionConfigurations = []
    for item in data:
        out.append(
            capo_sagemaker.types.collection_configuration.deserialize_aws_json_1_1(item)
        )
    return out
