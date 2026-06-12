"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.attribute_value
    import aws_sdk_gamelift.types.non_zero_and_max_string

PlayerAttributeMap: TypeAlias = dict[
    "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString",
    "aws_sdk_gamelift.types.attribute_value.AttributeValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PlayerAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_gamelift.types.attribute_value

        out[key] = aws_sdk_gamelift.types.attribute_value.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerAttributeMap:
    out: PlayerAttributeMap = {}
    for key, value in data.items():
        import aws_sdk_gamelift.types.attribute_value

        out[key] = aws_sdk_gamelift.types.attribute_value.deserialize_aws_json_1_1(
            value
        )
    return out
