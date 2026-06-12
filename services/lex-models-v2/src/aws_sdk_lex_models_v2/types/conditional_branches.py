"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConditionalBranches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conditional_branch

ConditionalBranches: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.conditional_branch.ConditionalBranch"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalBranches) -> list:
    import aws_sdk_lex_models_v2.types.conditional_branch

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.conditional_branch.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConditionalBranches:
    import aws_sdk_lex_models_v2.types.conditional_branch

    out: ConditionalBranches = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.conditional_branch.deserialize_json(item)
        )
    return out
