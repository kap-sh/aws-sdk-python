"""Generated from Smithy shape ``com.amazonaws.ssmsap#SubCheckResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.sub_check_result

SubCheckResultList: TypeAlias = list[
    "aws_sdk_ssm_sap.types.sub_check_result.SubCheckResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubCheckResultList) -> list:
    import aws_sdk_ssm_sap.types.sub_check_result

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.sub_check_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubCheckResultList:
    import aws_sdk_ssm_sap.types.sub_check_result

    out: SubCheckResultList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.sub_check_result.deserialize_json(item))
    return out
