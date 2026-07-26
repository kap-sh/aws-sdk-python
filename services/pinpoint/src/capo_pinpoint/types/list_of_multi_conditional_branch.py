"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfMultiConditionalBranch``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.multi_conditional_branch

ListOfMultiConditionalBranch: TypeAlias = list[
    "capo_pinpoint.types.multi_conditional_branch.MultiConditionalBranch"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfMultiConditionalBranch) -> list:
    import capo_pinpoint.types.multi_conditional_branch

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.multi_conditional_branch.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfMultiConditionalBranch:
    import capo_pinpoint.types.multi_conditional_branch

    out: ListOfMultiConditionalBranch = []
    for item in data:
        out.append(capo_pinpoint.types.multi_conditional_branch.deserialize_json(item))
    return out
