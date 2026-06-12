"""Generated from Smithy shape ``com.amazonaws.ecr#LayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.layer

LayerList: TypeAlias = list["aws_sdk_ecr.types.layer.Layer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerList) -> list:
    import aws_sdk_ecr.types.layer

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.layer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LayerList:
    import aws_sdk_ecr.types.layer

    out: LayerList = []
    for item in data:
        out.append(aws_sdk_ecr.types.layer.deserialize_aws_json_1_1(item))
    return out
