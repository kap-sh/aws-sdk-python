"""Generated from Smithy shape ``com.amazonaws.glue#Mappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.mapping

Mappings: TypeAlias = list["aws_sdk_glue.types.mapping.Mapping"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Mappings) -> list:
    import aws_sdk_glue.types.mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.mapping.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Mappings:
    import aws_sdk_glue.types.mapping

    out: Mappings = []
    for item in data:
        out.append(aws_sdk_glue.types.mapping.deserialize_aws_json_1_1(item))
    return out
