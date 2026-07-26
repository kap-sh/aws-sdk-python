"""Generated from Smithy shape ``com.amazonaws.machinelearning#DetailsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_machine_learning.types.details_attributes
    import capo_machine_learning.types.details_value

DetailsMap: TypeAlias = dict[
    "capo_machine_learning.types.details_attributes.DetailsAttributes",
    "capo_machine_learning.types.details_value.DetailsValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DetailsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_machine_learning.types.details_attributes

        out[
            capo_machine_learning.types.details_attributes.serialize_aws_json_1_1(key)
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> DetailsMap:
    out: DetailsMap = {}
    for key, value in data.items():
        import capo_machine_learning.types.details_attributes

        out[
            capo_machine_learning.types.details_attributes.deserialize_aws_json_1_1(key)
        ] = value
    return out
