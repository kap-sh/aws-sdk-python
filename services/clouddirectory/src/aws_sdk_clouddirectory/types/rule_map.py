"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RuleMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.rule
    import aws_sdk_clouddirectory.types.rule_key

RuleMap: TypeAlias = dict[
    "aws_sdk_clouddirectory.types.rule_key.RuleKey",
    "aws_sdk_clouddirectory.types.rule.Rule",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RuleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_clouddirectory.types.rule

        out[key] = aws_sdk_clouddirectory.types.rule.serialize_json(value)
    return out


def deserialize_json(data: dict) -> RuleMap:
    out: RuleMap = {}
    for key, value in data.items():
        import aws_sdk_clouddirectory.types.rule

        out[key] = aws_sdk_clouddirectory.types.rule.deserialize_json(value)
    return out
