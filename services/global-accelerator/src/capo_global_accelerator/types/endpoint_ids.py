"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string

EndpointIds: TypeAlias = list[
    "capo_global_accelerator.types.generic_string.GenericString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EndpointIds:
    return list(data)
