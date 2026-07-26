"""Generated from Smithy shape ``com.amazonaws.frauddetector#modelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.model

modelList: TypeAlias = list["capo_frauddetector.types.model.Model"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: modelList) -> list:
    import capo_frauddetector.types.model

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.model.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> modelList:
    import capo_frauddetector.types.model

    out: modelList = []
    for item in data:
        out.append(capo_frauddetector.types.model.deserialize_aws_json_1_1(item))
    return out
