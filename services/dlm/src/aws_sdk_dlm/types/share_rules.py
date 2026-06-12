"""Generated from Smithy shape ``com.amazonaws.dlm#ShareRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.share_rule

ShareRules: TypeAlias = list["aws_sdk_dlm.types.share_rule.ShareRule"]


# --- restJson1 ser/de ---
def serialize_json(value: ShareRules) -> list:
    import aws_sdk_dlm.types.share_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.share_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShareRules:
    import aws_sdk_dlm.types.share_rule

    out: ShareRules = []
    for item in data:
        out.append(aws_sdk_dlm.types.share_rule.deserialize_json(item))
    return out
