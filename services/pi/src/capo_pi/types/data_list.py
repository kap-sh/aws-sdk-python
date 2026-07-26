"""Generated from Smithy shape ``com.amazonaws.pi#DataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.data

DataList: TypeAlias = list["capo_pi.types.data.Data"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataList) -> list:
    import capo_pi.types.data

    out: list = []
    for item in value:
        out.append(capo_pi.types.data.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataList:
    import capo_pi.types.data

    out: DataList = []
    for item in data:
        out.append(capo_pi.types.data.deserialize_aws_json_1_1(item))
    return out
