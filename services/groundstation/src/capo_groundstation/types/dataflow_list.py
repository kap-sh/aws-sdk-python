"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.dataflow_detail

DataflowList: TypeAlias = list[
    "capo_groundstation.types.dataflow_detail.DataflowDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataflowList) -> list:
    import capo_groundstation.types.dataflow_detail

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.dataflow_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataflowList:
    import capo_groundstation.types.dataflow_detail

    out: DataflowList = []
    for item in data:
        out.append(capo_groundstation.types.dataflow_detail.deserialize_json(item))
    return out
