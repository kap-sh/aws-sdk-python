"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatumList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.datum

DatumList: TypeAlias = list["aws_sdk_iotsitewise.types.datum.Datum"]


# --- restJson1 ser/de ---
def serialize_json(value: DatumList) -> list:
    import aws_sdk_iotsitewise.types.datum

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.datum.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatumList:
    import aws_sdk_iotsitewise.types.datum

    out: DatumList = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.datum.deserialize_json(item))
    return out
