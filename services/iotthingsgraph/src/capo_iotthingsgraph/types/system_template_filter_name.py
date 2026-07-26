"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemTemplateFilterName``."""

from typing import Literal, TypeAlias, cast

SystemTemplateFilterName: TypeAlias = Literal["FLOW_TEMPLATE_ID",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTemplateFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SystemTemplateFilterName:
    return cast(SystemTemplateFilterName, data)
