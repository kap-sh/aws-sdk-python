"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ProcessorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.processor

ProcessorList: TypeAlias = list["capo_chime_sdk_messaging.types.processor.Processor"]


# --- restJson1 ser/de ---
def serialize_json(value: ProcessorList) -> list:
    import capo_chime_sdk_messaging.types.processor

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_messaging.types.processor.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProcessorList:
    import capo_chime_sdk_messaging.types.processor

    out: ProcessorList = []
    for item in data:
        out.append(capo_chime_sdk_messaging.types.processor.deserialize_json(item))
    return out
