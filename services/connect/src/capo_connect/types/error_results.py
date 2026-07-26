"""Generated from Smithy shape ``com.amazonaws.connect#ErrorResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.error_result

ErrorResults: TypeAlias = list["capo_connect.types.error_result.ErrorResult"]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorResults) -> list:
    import capo_connect.types.error_result

    out: list = []
    for item in value:
        out.append(capo_connect.types.error_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ErrorResults:
    import capo_connect.types.error_result

    out: ErrorResults = []
    for item in data:
        out.append(capo_connect.types.error_result.deserialize_json(item))
    return out
