"""Generated from Smithy shape ``com.amazonaws.pi#DataPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.data_point

DataPointsList: TypeAlias = list["aws_sdk_pi.types.data_point.DataPoint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataPointsList) -> list:
    import aws_sdk_pi.types.data_point

    out: list = []
    for item in value:
        out.append(aws_sdk_pi.types.data_point.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataPointsList:
    import aws_sdk_pi.types.data_point

    out: DataPointsList = []
    for item in data:
        out.append(aws_sdk_pi.types.data_point.deserialize_aws_json_1_1(item))
    return out
