"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowTemplateFilterName``."""

from typing import Literal, TypeAlias, cast

FlowTemplateFilterName: TypeAlias = Literal["DEVICE_MODEL_ID",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowTemplateFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlowTemplateFilterName:
    return cast(FlowTemplateFilterName, data)
