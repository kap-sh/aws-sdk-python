"""Generated from Smithy shape ``com.amazonaws.dlm#StagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.stage_values

StagesList: TypeAlias = list["aws_sdk_dlm.types.stage_values.StageValues"]


# --- restJson1 ser/de ---
def serialize_json(value: StagesList) -> list:
    import aws_sdk_dlm.types.stage_values

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.stage_values.serialize_json(item))
    return out


def deserialize_json(data: list) -> StagesList:
    import aws_sdk_dlm.types.stage_values

    out: StagesList = []
    for item in data:
        out.append(aws_sdk_dlm.types.stage_values.deserialize_json(item))
    return out
