"""Generated from Smithy shape ``com.amazonaws.applicationsignals#LogGroupReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.attributes

LogGroupReferences: TypeAlias = list[
    "aws_sdk_application_signals.types.attributes.Attributes"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupReferences) -> list:
    import aws_sdk_application_signals.types.attributes

    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.attributes.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogGroupReferences:
    import aws_sdk_application_signals.types.attributes

    out: LogGroupReferences = []
    for item in data:
        out.append(aws_sdk_application_signals.types.attributes.deserialize_json(item))
    return out
