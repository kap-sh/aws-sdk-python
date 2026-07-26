"""Generated from Smithy shape ``com.amazonaws.mgn#SplitConstructs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.split_construct

SplitConstructs: TypeAlias = list["capo_mgn.types.split_construct.SplitConstruct"]


# --- restJson1 ser/de ---
def serialize_json(value: SplitConstructs) -> list:
    import capo_mgn.types.split_construct

    out: list = []
    for item in value:
        out.append(capo_mgn.types.split_construct.serialize_json(item))
    return out


def deserialize_json(data: list) -> SplitConstructs:
    import capo_mgn.types.split_construct

    out: SplitConstructs = []
    for item in data:
        out.append(capo_mgn.types.split_construct.deserialize_json(item))
    return out
