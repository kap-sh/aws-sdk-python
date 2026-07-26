"""Generated from Smithy shape ``com.amazonaws.applicationsignals#LogGroupReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.attributes

LogGroupReferences: TypeAlias = list[
    "capo_application_signals.types.attributes.Attributes"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupReferences) -> list:
    import capo_application_signals.types.attributes

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.attributes.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogGroupReferences:
    import capo_application_signals.types.attributes

    out: LogGroupReferences = []
    for item in data:
        out.append(capo_application_signals.types.attributes.deserialize_json(item))
    return out
