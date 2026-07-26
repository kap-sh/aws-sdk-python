"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppInputSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_input_source

AppInputSourceList: TypeAlias = list[
    "capo_resiliencehub.types.app_input_source.AppInputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInputSourceList) -> list:
    import capo_resiliencehub.types.app_input_source

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.app_input_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppInputSourceList:
    import capo_resiliencehub.types.app_input_source

    out: AppInputSourceList = []
    for item in data:
        out.append(capo_resiliencehub.types.app_input_source.deserialize_json(item))
    return out
