"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetectionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.general_labels_settings


class LabelDetectionSettings(TypedDict, closed=True):
    general_labels: NotRequired[
        "capo_rekognition.types.general_labels_settings.GeneralLabelsSettings"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelDetectionSettings) -> dict:
    out: dict = {}
    if "general_labels" in value:
        import capo_rekognition.types.general_labels_settings

        out["GeneralLabels"] = (
            capo_rekognition.types.general_labels_settings.serialize_aws_json_1_1(
                value["general_labels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelDetectionSettings:
    out: LabelDetectionSettings = {}  # type: ignore[typeddict-item]
    if "GeneralLabels" in data:
        import capo_rekognition.types.general_labels_settings

        out["general_labels"] = (
            capo_rekognition.types.general_labels_settings.deserialize_aws_json_1_1(
                data["GeneralLabels"]
            )
        )
    return out
