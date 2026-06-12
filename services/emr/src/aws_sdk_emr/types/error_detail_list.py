"""Generated from Smithy shape ``com.amazonaws.emr#ErrorDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.error_detail

ErrorDetailList: TypeAlias = list["aws_sdk_emr.types.error_detail.ErrorDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetailList) -> list:
    import aws_sdk_emr.types.error_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.error_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ErrorDetailList:
    import aws_sdk_emr.types.error_detail

    out: ErrorDetailList = []
    for item in data:
        out.append(aws_sdk_emr.types.error_detail.deserialize_aws_json_1_1(item))
    return out
