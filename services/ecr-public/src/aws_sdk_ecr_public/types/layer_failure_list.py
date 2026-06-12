"""Generated from Smithy shape ``com.amazonaws.ecrpublic#LayerFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.layer_failure

LayerFailureList: TypeAlias = list[
    "aws_sdk_ecr_public.types.layer_failure.LayerFailure"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerFailureList) -> list:
    import aws_sdk_ecr_public.types.layer_failure

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr_public.types.layer_failure.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LayerFailureList:
    import aws_sdk_ecr_public.types.layer_failure

    out: LayerFailureList = []
    for item in data:
        out.append(
            aws_sdk_ecr_public.types.layer_failure.deserialize_aws_json_1_1(item)
        )
    return out
