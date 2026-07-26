"""Generated from Smithy shape ``com.amazonaws.dlm#ShareRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.share_rule

ShareRules: TypeAlias = list["capo_dlm.types.share_rule.ShareRule"]


# --- restJson1 ser/de ---
def serialize_json(value: ShareRules) -> list:
    import capo_dlm.types.share_rule

    out: list = []
    for item in value:
        out.append(capo_dlm.types.share_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShareRules:
    import capo_dlm.types.share_rule

    out: ShareRules = []
    for item in data:
        out.append(capo_dlm.types.share_rule.deserialize_json(item))
    return out
