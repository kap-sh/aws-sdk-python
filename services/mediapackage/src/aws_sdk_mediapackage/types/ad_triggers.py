"""Generated from Smithy shape ``com.amazonaws.mediapackage#AdTriggers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__ad_triggers_element

AdTriggers: TypeAlias = list[
    "aws_sdk_mediapackage.types.__ad_triggers_element.__AdTriggersElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdTriggers) -> list:
    import aws_sdk_mediapackage.types.__ad_triggers_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackage.types.__ad_triggers_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AdTriggers:
    import aws_sdk_mediapackage.types.__ad_triggers_element

    out: AdTriggers = []
    for item in data:
        out.append(
            aws_sdk_mediapackage.types.__ad_triggers_element.deserialize_json(item)
        )
    return out
