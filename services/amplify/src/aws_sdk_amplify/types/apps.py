"""Generated from Smithy shape ``com.amazonaws.amplify#Apps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app

Apps: TypeAlias = list["aws_sdk_amplify.types.app.App"]


# --- restJson1 ser/de ---
def serialize_json(value: Apps) -> list:
    import aws_sdk_amplify.types.app

    out: list = []
    for item in value:
        out.append(aws_sdk_amplify.types.app.serialize_json(item))
    return out


def deserialize_json(data: list) -> Apps:
    import aws_sdk_amplify.types.app

    out: Apps = []
    for item in data:
        out.append(aws_sdk_amplify.types.app.deserialize_json(item))
    return out
