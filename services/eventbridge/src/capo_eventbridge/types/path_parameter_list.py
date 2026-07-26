"""Generated from Smithy shape ``com.amazonaws.eventbridge#PathParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.path_parameter

PathParameterList: TypeAlias = list[
    "capo_eventbridge.types.path_parameter.PathParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PathParameterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PathParameterList:
    return list(data)
