"""Generated from Smithy shape ``com.amazonaws.glue#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.filter_value

FilterValues: TypeAlias = list["aws_sdk_glue.types.filter_value.FilterValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterValues) -> list:
    import aws_sdk_glue.types.filter_value

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.filter_value.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterValues:
    import aws_sdk_glue.types.filter_value

    out: FilterValues = []
    for item in data:
        out.append(aws_sdk_glue.types.filter_value.deserialize_aws_json_1_1(item))
    return out
