"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfCore``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.core

__listOfCore: TypeAlias = list["aws_sdk_greengrass.types.core.Core"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCore) -> list:
    import aws_sdk_greengrass.types.core

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.core.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCore:
    import aws_sdk_greengrass.types.core

    out: __listOfCore = []
    for item in data:
        out.append(aws_sdk_greengrass.types.core.deserialize_json(item))
    return out
