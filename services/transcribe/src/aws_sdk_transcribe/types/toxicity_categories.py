"""Generated from Smithy shape ``com.amazonaws.transcribe#ToxicityCategories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.toxicity_category

ToxicityCategories: TypeAlias = list[
    "aws_sdk_transcribe.types.toxicity_category.ToxicityCategory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToxicityCategories) -> list:
    import aws_sdk_transcribe.types.toxicity_category

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe.types.toxicity_category.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ToxicityCategories:
    import aws_sdk_transcribe.types.toxicity_category

    out: ToxicityCategories = []
    for item in data:
        out.append(
            aws_sdk_transcribe.types.toxicity_category.deserialize_aws_json_1_1(item)
        )
    return out
