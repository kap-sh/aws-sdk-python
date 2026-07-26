"""Generated from Smithy shape ``com.amazonaws.lakeformation#WriteOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.write_operation

WriteOperationList: TypeAlias = list[
    "capo_lakeformation.types.write_operation.WriteOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: WriteOperationList) -> list:
    import capo_lakeformation.types.write_operation

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.write_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> WriteOperationList:
    import capo_lakeformation.types.write_operation

    out: WriteOperationList = []
    for item in data:
        out.append(capo_lakeformation.types.write_operation.deserialize_json(item))
    return out
