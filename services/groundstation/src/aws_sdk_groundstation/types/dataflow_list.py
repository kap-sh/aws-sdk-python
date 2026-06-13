"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.dataflow_detail

DataflowList: TypeAlias = list[
    "aws_sdk_groundstation.types.dataflow_detail.DataflowDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataflowList) -> list:
    import aws_sdk_groundstation.types.dataflow_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.dataflow_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataflowList:
    import aws_sdk_groundstation.types.dataflow_detail

    out: DataflowList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.dataflow_detail.deserialize_json(item))
    return out
