"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationSourcePropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.integration_string

IntegrationSourcePropertiesMap: TypeAlias = dict[
    "capo_glue.types.integration_string.IntegrationString",
    "capo_glue.types.integration_string.IntegrationString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: IntegrationSourcePropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationSourcePropertiesMap:
    out: IntegrationSourcePropertiesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
