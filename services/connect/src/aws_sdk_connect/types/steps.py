"""Generated from Smithy shape ``com.amazonaws.connect#Steps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.step

Steps: TypeAlias = list["aws_sdk_connect.types.step.Step"]


# --- restJson1 ser/de ---
def serialize_json(value: Steps) -> list:
    import aws_sdk_connect.types.step

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.step.serialize_json(item))
    return out


def deserialize_json(data: list) -> Steps:
    import aws_sdk_connect.types.step

    out: Steps = []
    for item in data:
        out.append(aws_sdk_connect.types.step.deserialize_json(item))
    return out
