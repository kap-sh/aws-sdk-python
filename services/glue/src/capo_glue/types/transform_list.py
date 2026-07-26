"""Generated from Smithy shape ``com.amazonaws.glue#TransformList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.ml_transform

TransformList: TypeAlias = list["capo_glue.types.ml_transform.MLTransform"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformList) -> list:
    import capo_glue.types.ml_transform

    out: list = []
    for item in value:
        out.append(capo_glue.types.ml_transform.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TransformList:
    import capo_glue.types.ml_transform

    out: TransformList = []
    for item in data:
        out.append(capo_glue.types.ml_transform.deserialize_aws_json_1_1(item))
    return out
