"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ErrorDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.error_detail

ErrorDetailList: TypeAlias = list["capo_resiliencehub.types.error_detail.ErrorDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetailList) -> list:
    import capo_resiliencehub.types.error_detail

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.error_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ErrorDetailList:
    import capo_resiliencehub.types.error_detail

    out: ErrorDetailList = []
    for item in data:
        out.append(capo_resiliencehub.types.error_detail.deserialize_json(item))
    return out
