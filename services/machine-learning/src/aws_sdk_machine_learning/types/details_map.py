"""Generated from Smithy shape ``com.amazonaws.machinelearning#DetailsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.details_attributes
    import aws_sdk_machine_learning.types.details_value

DetailsMap: TypeAlias = dict[
    "aws_sdk_machine_learning.types.details_attributes.DetailsAttributes",
    "aws_sdk_machine_learning.types.details_value.DetailsValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DetailsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_machine_learning.types.details_attributes

        out[
            aws_sdk_machine_learning.types.details_attributes.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> DetailsMap:
    out: DetailsMap = {}
    for key, value in data.items():
        import aws_sdk_machine_learning.types.details_attributes

        out[
            aws_sdk_machine_learning.types.details_attributes.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out
