"""Generated from Smithy shape ``com.amazonaws.textract#UndetectedSignatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.undetected_signature

UndetectedSignatureList: TypeAlias = list[
    "aws_sdk_textract.types.undetected_signature.UndetectedSignature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UndetectedSignatureList) -> list:
    import aws_sdk_textract.types.undetected_signature

    out: list = []
    for item in value:
        out.append(
            aws_sdk_textract.types.undetected_signature.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UndetectedSignatureList:
    import aws_sdk_textract.types.undetected_signature

    out: UndetectedSignatureList = []
    for item in data:
        out.append(
            aws_sdk_textract.types.undetected_signature.deserialize_aws_json_1_1(item)
        )
    return out
