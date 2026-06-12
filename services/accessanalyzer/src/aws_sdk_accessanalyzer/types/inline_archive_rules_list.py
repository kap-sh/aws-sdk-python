"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InlineArchiveRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.inline_archive_rule

InlineArchiveRulesList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.inline_archive_rule.InlineArchiveRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: InlineArchiveRulesList) -> list:
    import aws_sdk_accessanalyzer.types.inline_archive_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.inline_archive_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InlineArchiveRulesList:
    import aws_sdk_accessanalyzer.types.inline_archive_rule

    out: InlineArchiveRulesList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.inline_archive_rule.deserialize_json(item)
        )
    return out
