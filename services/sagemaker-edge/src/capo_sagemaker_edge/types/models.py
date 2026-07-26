"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#Models``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.model

Models: TypeAlias = list["capo_sagemaker_edge.types.model.Model"]


# --- restJson1 ser/de ---
def serialize_json(value: Models) -> list:
    import capo_sagemaker_edge.types.model

    out: list = []
    for item in value:
        out.append(capo_sagemaker_edge.types.model.serialize_json(item))
    return out


def deserialize_json(data: list) -> Models:
    import capo_sagemaker_edge.types.model

    out: Models = []
    for item in data:
        out.append(capo_sagemaker_edge.types.model.deserialize_json(item))
    return out
