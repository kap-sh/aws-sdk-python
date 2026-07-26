"""Generated from Smithy shape ``com.amazonaws.pi#DataPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.data_point

DataPointsList: TypeAlias = list["capo_pi.types.data_point.DataPoint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataPointsList) -> list:
    import capo_pi.types.data_point

    out: list = []
    for item in value:
        out.append(capo_pi.types.data_point.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataPointsList:
    import capo_pi.types.data_point

    out: DataPointsList = []
    for item in data:
        out.append(capo_pi.types.data_point.deserialize_aws_json_1_1(item))
    return out
