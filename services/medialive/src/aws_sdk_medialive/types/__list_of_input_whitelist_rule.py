"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputWhitelistRule``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_whitelist_rule

__listOfInputWhitelistRule: TypeAlias = list[
    "aws_sdk_medialive.types.input_whitelist_rule.InputWhitelistRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputWhitelistRule) -> list:
    import aws_sdk_medialive.types.input_whitelist_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_whitelist_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputWhitelistRule:
    import aws_sdk_medialive.types.input_whitelist_rule

    out: __listOfInputWhitelistRule = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_whitelist_rule.deserialize_json(item))
    return out
