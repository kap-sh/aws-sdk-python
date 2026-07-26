"""Generated from Smithy shape ``com.amazonaws.forecast#AttributeConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.attribute_config

AttributeConfigs: TypeAlias = list[
    "capo_forecast.types.attribute_config.AttributeConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeConfigs) -> list:
    import capo_forecast.types.attribute_config

    out: list = []
    for item in value:
        out.append(capo_forecast.types.attribute_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttributeConfigs:
    import capo_forecast.types.attribute_config

    out: AttributeConfigs = []
    for item in data:
        out.append(capo_forecast.types.attribute_config.deserialize_aws_json_1_1(item))
    return out
