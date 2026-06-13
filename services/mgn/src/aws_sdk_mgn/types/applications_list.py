"""Generated from Smithy shape ``com.amazonaws.mgn#ApplicationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.application

ApplicationsList: TypeAlias = list["aws_sdk_mgn.types.application.Application"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationsList) -> list:
    import aws_sdk_mgn.types.application

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.application.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationsList:
    import aws_sdk_mgn.types.application

    out: ApplicationsList = []
    for item in data:
        out.append(aws_sdk_mgn.types.application.deserialize_json(item))
    return out
