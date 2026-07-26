"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfExternalModelOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.external_model_outputs

ListOfExternalModelOutputs: TypeAlias = list[
    "capo_frauddetector.types.external_model_outputs.ExternalModelOutputs"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfExternalModelOutputs) -> list:
    import capo_frauddetector.types.external_model_outputs

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.external_model_outputs.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfExternalModelOutputs:
    import capo_frauddetector.types.external_model_outputs

    out: ListOfExternalModelOutputs = []
    for item in data:
        out.append(
            capo_frauddetector.types.external_model_outputs.deserialize_aws_json_1_1(
                item
            )
        )
    return out
