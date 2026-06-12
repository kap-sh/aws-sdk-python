"""Generated from Smithy shape ``com.amazonaws.textract#SignatureDetectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.signature_detection

SignatureDetectionList: TypeAlias = list[
    "aws_sdk_textract.types.signature_detection.SignatureDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignatureDetectionList) -> list:
    import aws_sdk_textract.types.signature_detection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_textract.types.signature_detection.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SignatureDetectionList:
    import aws_sdk_textract.types.signature_detection

    out: SignatureDetectionList = []
    for item in data:
        out.append(
            aws_sdk_textract.types.signature_detection.deserialize_aws_json_1_1(item)
        )
    return out
