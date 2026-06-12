"""Generated from Smithy shape ``com.amazonaws.translate#AppliedTerminologyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_translate.types.applied_terminology

AppliedTerminologyList: TypeAlias = list[
    "aws_sdk_translate.types.applied_terminology.AppliedTerminology"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppliedTerminologyList) -> list:
    import aws_sdk_translate.types.applied_terminology

    out: list = []
    for item in value:
        out.append(
            aws_sdk_translate.types.applied_terminology.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AppliedTerminologyList:
    import aws_sdk_translate.types.applied_terminology

    out: AppliedTerminologyList = []
    for item in data:
        out.append(
            aws_sdk_translate.types.applied_terminology.deserialize_aws_json_1_1(item)
        )
    return out
