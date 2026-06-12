"""Generated from Smithy shape ``com.amazonaws.ssm#PatchCVEIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch_cve_id

PatchCVEIdList: TypeAlias = list["aws_sdk_ssm.types.patch_cve_id.PatchCVEId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchCVEIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PatchCVEIdList:
    return list(data)
