"""Generated from Smithy shape ``com.amazonaws.glue#DevEndpointNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.generic_string

DevEndpointNames: TypeAlias = list["capo_glue.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevEndpointNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DevEndpointNames:
    return list(data)
