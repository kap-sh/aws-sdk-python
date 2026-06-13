"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#SuggestedFixes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.suggested_fix

SuggestedFixes: TypeAlias = list[
    "aws_sdk_codeguru_security.types.suggested_fix.SuggestedFix"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedFixes) -> list:
    import aws_sdk_codeguru_security.types.suggested_fix

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguru_security.types.suggested_fix.serialize_json(item))
    return out


def deserialize_json(data: list) -> SuggestedFixes:
    import aws_sdk_codeguru_security.types.suggested_fix

    out: SuggestedFixes = []
    for item in data:
        out.append(aws_sdk_codeguru_security.types.suggested_fix.deserialize_json(item))
    return out
