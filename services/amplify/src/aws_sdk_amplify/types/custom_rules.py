"""Generated from Smithy shape ``com.amazonaws.amplify#CustomRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.custom_rule

CustomRules: TypeAlias = list["aws_sdk_amplify.types.custom_rule.CustomRule"]


# --- restJson1 ser/de ---
def serialize_json(value: CustomRules) -> list:
    import aws_sdk_amplify.types.custom_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_amplify.types.custom_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomRules:
    import aws_sdk_amplify.types.custom_rule

    out: CustomRules = []
    for item in data:
        out.append(aws_sdk_amplify.types.custom_rule.deserialize_json(item))
    return out
