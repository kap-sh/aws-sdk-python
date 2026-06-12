"""Generated from Smithy shape ``com.amazonaws.frauddetector#labelMapper``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.list_of_strings
    import aws_sdk_frauddetector.types.string

labelMapper: TypeAlias = dict[
    "aws_sdk_frauddetector.types.string.string",
    "aws_sdk_frauddetector.types.list_of_strings.ListOfStrings",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: labelMapper) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_frauddetector.types.list_of_strings

        out[key] = aws_sdk_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> labelMapper:
    out: labelMapper = {}
    for key, value in data.items():
        import aws_sdk_frauddetector.types.list_of_strings

        out[key] = aws_sdk_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
            value
        )
    return out
