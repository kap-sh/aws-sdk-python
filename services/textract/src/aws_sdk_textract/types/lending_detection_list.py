"""Generated from Smithy shape ``com.amazonaws.textract#LendingDetectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.lending_detection

LendingDetectionList: TypeAlias = list[
    "aws_sdk_textract.types.lending_detection.LendingDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingDetectionList) -> list:
    import aws_sdk_textract.types.lending_detection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_textract.types.lending_detection.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LendingDetectionList:
    import aws_sdk_textract.types.lending_detection

    out: LendingDetectionList = []
    for item in data:
        out.append(
            aws_sdk_textract.types.lending_detection.deserialize_aws_json_1_1(item)
        )
    return out
