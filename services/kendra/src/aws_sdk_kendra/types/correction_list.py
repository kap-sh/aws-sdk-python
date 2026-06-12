"""Generated from Smithy shape ``com.amazonaws.kendra#CorrectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.correction

CorrectionList: TypeAlias = list["aws_sdk_kendra.types.correction.Correction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CorrectionList) -> list:
    import aws_sdk_kendra.types.correction

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.correction.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CorrectionList:
    import aws_sdk_kendra.types.correction

    out: CorrectionList = []
    for item in data:
        out.append(aws_sdk_kendra.types.correction.deserialize_aws_json_1_1(item))
    return out
