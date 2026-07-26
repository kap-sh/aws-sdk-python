"""Generated from Smithy shape ``com.amazonaws.rekognition#ModerationLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.moderation_label

ModerationLabels: TypeAlias = list[
    "capo_rekognition.types.moderation_label.ModerationLabel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModerationLabels) -> list:
    import capo_rekognition.types.moderation_label

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.moderation_label.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ModerationLabels:
    import capo_rekognition.types.moderation_label

    out: ModerationLabels = []
    for item in data:
        out.append(
            capo_rekognition.types.moderation_label.deserialize_aws_json_1_1(item)
        )
    return out
