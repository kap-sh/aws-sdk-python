"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionTagRuleConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.session_tag_key

RowLevelPermissionTagRuleConfiguration: TypeAlias = list[
    "capo_quicksight.types.session_tag_key.SessionTagKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionTagRuleConfiguration) -> list:
    return list(value)


def deserialize_json(data: list) -> RowLevelPermissionTagRuleConfiguration:
    return list(data)
