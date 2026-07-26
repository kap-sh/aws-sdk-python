"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.lf_tag_error

LFTagErrors: TypeAlias = list["capo_lakeformation.types.lf_tag_error.LFTagError"]


# --- restJson1 ser/de ---
def serialize_json(value: LFTagErrors) -> list:
    import capo_lakeformation.types.lf_tag_error

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.lf_tag_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> LFTagErrors:
    import capo_lakeformation.types.lf_tag_error

    out: LFTagErrors = []
    for item in data:
        out.append(capo_lakeformation.types.lf_tag_error.deserialize_json(item))
    return out
