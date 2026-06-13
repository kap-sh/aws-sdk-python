"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_type

ApplicationTypeList: TypeAlias = list[
    "aws_sdk_ssm_sap.types.application_type.ApplicationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationTypeList) -> list:
    import aws_sdk_ssm_sap.types.application_type

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.application_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationTypeList:
    import aws_sdk_ssm_sap.types.application_type

    out: ApplicationTypeList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.application_type.deserialize_json(item))
    return out
