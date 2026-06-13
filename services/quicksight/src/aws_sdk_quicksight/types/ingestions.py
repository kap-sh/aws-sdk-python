"""Generated from Smithy shape ``com.amazonaws.quicksight#Ingestions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.ingestion

Ingestions: TypeAlias = list["aws_sdk_quicksight.types.ingestion.Ingestion"]


# --- restJson1 ser/de ---
def serialize_json(value: Ingestions) -> list:
    import aws_sdk_quicksight.types.ingestion

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.ingestion.serialize_json(item))
    return out


def deserialize_json(data: list) -> Ingestions:
    import aws_sdk_quicksight.types.ingestion

    out: Ingestions = []
    for item in data:
        out.append(aws_sdk_quicksight.types.ingestion.deserialize_json(item))
    return out
