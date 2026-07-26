"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InlineArchiveRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.inline_archive_rule

InlineArchiveRulesList: TypeAlias = list[
    "capo_accessanalyzer.types.inline_archive_rule.InlineArchiveRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: InlineArchiveRulesList) -> list:
    import capo_accessanalyzer.types.inline_archive_rule

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.inline_archive_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> InlineArchiveRulesList:
    import capo_accessanalyzer.types.inline_archive_rule

    out: InlineArchiveRulesList = []
    for item in data:
        out.append(capo_accessanalyzer.types.inline_archive_rule.deserialize_json(item))
    return out
