"""Generated from Smithy shape ``com.amazonaws.rekognition#StartSegmentDetectionFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.start_shot_detection_filter
    import aws_sdk_rekognition.types.start_technical_cue_detection_filter


class StartSegmentDetectionFilters(TypedDict):
    technical_cue_filter: NotRequired[
        "aws_sdk_rekognition.types.start_technical_cue_detection_filter.StartTechnicalCueDetectionFilter"
    ]
    """<p>Filters that are specific to technical cues.</p>"""
    shot_filter: NotRequired[
        "aws_sdk_rekognition.types.start_shot_detection_filter.StartShotDetectionFilter"
    ]
    """<p>Filters that are specific to shot detections.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSegmentDetectionFilters) -> dict:
    out: dict = {}
    if "technical_cue_filter" in value:
        import aws_sdk_rekognition.types.start_technical_cue_detection_filter

        out["TechnicalCueFilter"] = (
            aws_sdk_rekognition.types.start_technical_cue_detection_filter.serialize_aws_json_1_1(
                value["technical_cue_filter"]
            )
        )
    if "shot_filter" in value:
        import aws_sdk_rekognition.types.start_shot_detection_filter

        out["ShotFilter"] = (
            aws_sdk_rekognition.types.start_shot_detection_filter.serialize_aws_json_1_1(
                value["shot_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSegmentDetectionFilters:
    out: StartSegmentDetectionFilters = {}  # type: ignore[typeddict-item]
    if "TechnicalCueFilter" in data:
        import aws_sdk_rekognition.types.start_technical_cue_detection_filter

        out["technical_cue_filter"] = (
            aws_sdk_rekognition.types.start_technical_cue_detection_filter.deserialize_aws_json_1_1(
                data["TechnicalCueFilter"]
            )
        )
    if "ShotFilter" in data:
        import aws_sdk_rekognition.types.start_shot_detection_filter

        out["shot_filter"] = (
            aws_sdk_rekognition.types.start_shot_detection_filter.deserialize_aws_json_1_1(
                data["ShotFilter"]
            )
        )
    return out
