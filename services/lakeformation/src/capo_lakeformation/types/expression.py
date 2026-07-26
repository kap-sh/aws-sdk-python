"""Generated from Smithy shape ``com.amazonaws.lakeformation#Expression``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.lf_tag

Expression: TypeAlias = list["capo_lakeformation.types.lf_tag.LFTag"]


# --- restJson1 ser/de ---
def serialize_json(value: Expression) -> list:
    import capo_lakeformation.types.lf_tag

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.lf_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> Expression:
    import capo_lakeformation.types.lf_tag

    out: Expression = []
    for item in data:
        out.append(capo_lakeformation.types.lf_tag.deserialize_json(item))
    return out
