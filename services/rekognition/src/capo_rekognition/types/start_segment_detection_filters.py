"""Generated from Smithy shape ``com.amazonaws.rekognition#StartSegmentDetectionFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.start_shot_detection_filter
    import capo_rekognition.types.start_technical_cue_detection_filter


class StartSegmentDetectionFilters(TypedDict, closed=True):
    technical_cue_filter: NotRequired[
        "capo_rekognition.types.start_technical_cue_detection_filter.StartTechnicalCueDetectionFilter"
    ]
    """<p>Filters that are specific to technical cues.</p>"""
    shot_filter: NotRequired[
        "capo_rekognition.types.start_shot_detection_filter.StartShotDetectionFilter"
    ]
    """<p>Filters that are specific to shot detections.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSegmentDetectionFilters) -> dict:
    out: dict = {}
    if "technical_cue_filter" in value:
        import capo_rekognition.types.start_technical_cue_detection_filter

        out["TechnicalCueFilter"] = (
            capo_rekognition.types.start_technical_cue_detection_filter.serialize_aws_json_1_1(
                value["technical_cue_filter"]
            )
        )
    if "shot_filter" in value:
        import capo_rekognition.types.start_shot_detection_filter

        out["ShotFilter"] = (
            capo_rekognition.types.start_shot_detection_filter.serialize_aws_json_1_1(
                value["shot_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSegmentDetectionFilters:
    out: StartSegmentDetectionFilters = {}  # type: ignore[typeddict-item]
    if "TechnicalCueFilter" in data:
        import capo_rekognition.types.start_technical_cue_detection_filter

        out["technical_cue_filter"] = (
            capo_rekognition.types.start_technical_cue_detection_filter.deserialize_aws_json_1_1(
                data["TechnicalCueFilter"]
            )
        )
    if "ShotFilter" in data:
        import capo_rekognition.types.start_shot_detection_filter

        out["shot_filter"] = (
            capo_rekognition.types.start_shot_detection_filter.deserialize_aws_json_1_1(
                data["ShotFilter"]
            )
        )
    return out
