"""Generated from Smithy shape ``com.amazonaws.greengrass#ErrorDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.error_detail

ErrorDetails: TypeAlias = list["capo_greengrass.types.error_detail.ErrorDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> list:
    import capo_greengrass.types.error_detail

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.error_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ErrorDetails:
    import capo_greengrass.types.error_detail

    out: ErrorDetails = []
    for item in data:
        out.append(capo_greengrass.types.error_detail.deserialize_json(item))
    return out
