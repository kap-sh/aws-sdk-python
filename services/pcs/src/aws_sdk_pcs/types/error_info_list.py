"""Generated from Smithy shape ``com.amazonaws.pcs#ErrorInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pcs.types.error_info

ErrorInfoList: TypeAlias = list["aws_sdk_pcs.types.error_info.ErrorInfo"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorInfoList) -> list:
    import aws_sdk_pcs.types.error_info

    out: list = []
    for item in value:
        out.append(aws_sdk_pcs.types.error_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ErrorInfoList:
    import aws_sdk_pcs.types.error_info

    out: ErrorInfoList = []
    for item in data:
        out.append(aws_sdk_pcs.types.error_info.deserialize_aws_json_1_0(item))
    return out
