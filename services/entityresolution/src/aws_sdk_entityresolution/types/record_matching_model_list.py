"""Generated from Smithy shape ``com.amazonaws.entityresolution#RecordMatchingModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.record_matching_model

RecordMatchingModelList: TypeAlias = list[
    "aws_sdk_entityresolution.types.record_matching_model.RecordMatchingModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordMatchingModelList) -> list:
    import aws_sdk_entityresolution.types.record_matching_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.record_matching_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecordMatchingModelList:
    import aws_sdk_entityresolution.types.record_matching_model

    out: RecordMatchingModelList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.record_matching_model.deserialize_json(item)
        )
    return out
