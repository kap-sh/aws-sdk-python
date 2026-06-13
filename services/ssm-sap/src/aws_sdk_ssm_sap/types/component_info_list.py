"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.component_info

ComponentInfoList: TypeAlias = list[
    "aws_sdk_ssm_sap.types.component_info.ComponentInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentInfoList) -> list:
    import aws_sdk_ssm_sap.types.component_info

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.component_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentInfoList:
    import aws_sdk_ssm_sap.types.component_info

    out: ComponentInfoList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.component_info.deserialize_json(item))
    return out
