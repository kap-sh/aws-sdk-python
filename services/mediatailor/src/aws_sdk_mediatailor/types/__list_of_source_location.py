"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfSourceLocation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.source_location

__listOfSourceLocation: TypeAlias = list[
    "aws_sdk_mediatailor.types.source_location.SourceLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSourceLocation) -> list:
    import aws_sdk_mediatailor.types.source_location

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.source_location.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSourceLocation:
    import aws_sdk_mediatailor.types.source_location

    out: __listOfSourceLocation = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.source_location.deserialize_json(item))
    return out
