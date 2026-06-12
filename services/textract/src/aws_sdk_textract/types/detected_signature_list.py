"""Generated from Smithy shape ``com.amazonaws.textract#DetectedSignatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.detected_signature

DetectedSignatureList: TypeAlias = list[
    "aws_sdk_textract.types.detected_signature.DetectedSignature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectedSignatureList) -> list:
    import aws_sdk_textract.types.detected_signature

    out: list = []
    for item in value:
        out.append(
            aws_sdk_textract.types.detected_signature.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DetectedSignatureList:
    import aws_sdk_textract.types.detected_signature

    out: DetectedSignatureList = []
    for item in data:
        out.append(
            aws_sdk_textract.types.detected_signature.deserialize_aws_json_1_1(item)
        )
    return out
