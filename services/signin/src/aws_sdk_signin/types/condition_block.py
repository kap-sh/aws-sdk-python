"""Generated from Smithy shape ``com.amazonaws.signin#ConditionBlock``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_signin.types.condition
    import aws_sdk_signin.types.condition_type

ConditionBlock: TypeAlias = dict[
    "aws_sdk_signin.types.condition_type.ConditionType",
    "aws_sdk_signin.types.condition.Condition",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConditionBlock) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_signin.types.condition

        out[key] = aws_sdk_signin.types.condition.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ConditionBlock:
    out: ConditionBlock = {}
    for key, value in data.items():
        import aws_sdk_signin.types.condition

        out[key] = aws_sdk_signin.types.condition.deserialize_json(value)
    return out
