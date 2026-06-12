"""Generated from Smithy shape ``com.amazonaws.codecatalyst#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.filter

Filters: TypeAlias = list["aws_sdk_codecatalyst.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: Filters) -> list:
    import aws_sdk_codecatalyst.types.filter

    out: list = []
    for item in value:
        out.append(aws_sdk_codecatalyst.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> Filters:
    import aws_sdk_codecatalyst.types.filter

    out: Filters = []
    for item in data:
        out.append(aws_sdk_codecatalyst.types.filter.deserialize_json(item))
    return out
