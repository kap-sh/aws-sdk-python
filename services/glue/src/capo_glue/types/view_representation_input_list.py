"""Generated from Smithy shape ``com.amazonaws.glue#ViewRepresentationInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.view_representation_input

ViewRepresentationInputList: TypeAlias = list[
    "capo_glue.types.view_representation_input.ViewRepresentationInput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewRepresentationInputList) -> list:
    import capo_glue.types.view_representation_input

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.view_representation_input.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ViewRepresentationInputList:
    import capo_glue.types.view_representation_input

    out: ViewRepresentationInputList = []
    for item in data:
        out.append(
            capo_glue.types.view_representation_input.deserialize_aws_json_1_1(item)
        )
    return out
