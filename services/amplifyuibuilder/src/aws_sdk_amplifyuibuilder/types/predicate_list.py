"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#PredicateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.predicate

PredicateList: TypeAlias = list["aws_sdk_amplifyuibuilder.types.predicate.Predicate"]


# --- restJson1 ser/de ---
def serialize_json(value: PredicateList) -> list:
    import aws_sdk_amplifyuibuilder.types.predicate

    out: list = []
    for item in value:
        out.append(aws_sdk_amplifyuibuilder.types.predicate.serialize_json(item))
    return out


def deserialize_json(data: list) -> PredicateList:
    import aws_sdk_amplifyuibuilder.types.predicate

    out: PredicateList = []
    for item in data:
        out.append(aws_sdk_amplifyuibuilder.types.predicate.deserialize_json(item))
    return out
