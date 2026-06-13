"""Generated from Smithy shape ``com.amazonaws.neptunedata#PropertygraphRecordsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.propertygraph_record

PropertygraphRecordsList: TypeAlias = list[
    "aws_sdk_neptunedata.types.propertygraph_record.PropertygraphRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertygraphRecordsList) -> list:
    import aws_sdk_neptunedata.types.propertygraph_record

    out: list = []
    for item in value:
        out.append(aws_sdk_neptunedata.types.propertygraph_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> PropertygraphRecordsList:
    import aws_sdk_neptunedata.types.propertygraph_record

    out: PropertygraphRecordsList = []
    for item in data:
        out.append(
            aws_sdk_neptunedata.types.propertygraph_record.deserialize_json(item)
        )
    return out
