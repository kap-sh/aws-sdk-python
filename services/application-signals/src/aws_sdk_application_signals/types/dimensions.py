"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Dimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.dimension

Dimensions: TypeAlias = list["aws_sdk_application_signals.types.dimension.Dimension"]


# --- restJson1 ser/de ---
def serialize_json(value: Dimensions) -> list:
    import aws_sdk_application_signals.types.dimension

    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.dimension.serialize_json(item))
    return out


def deserialize_json(data: list) -> Dimensions:
    import aws_sdk_application_signals.types.dimension

    out: Dimensions = []
    for item in data:
        out.append(aws_sdk_application_signals.types.dimension.deserialize_json(item))
    return out
