"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeDominantLanguageDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dominant_language_detection_job_properties


class DescribeDominantLanguageDetectionJobResponse(TypedDict, closed=True):
    dominant_language_detection_job_properties: NotRequired[
        "aws_sdk_comprehend.types.dominant_language_detection_job_properties.DominantLanguageDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with a dominant language detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDominantLanguageDetectionJobResponse) -> dict:
    out: dict = {}
    if "dominant_language_detection_job_properties" in value:
        import aws_sdk_comprehend.types.dominant_language_detection_job_properties

        out["DominantLanguageDetectionJobProperties"] = (
            aws_sdk_comprehend.types.dominant_language_detection_job_properties.serialize_aws_json_1_1(
                value["dominant_language_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeDominantLanguageDetectionJobResponse:
    out: DescribeDominantLanguageDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "DominantLanguageDetectionJobProperties" in data:
        import aws_sdk_comprehend.types.dominant_language_detection_job_properties

        out["dominant_language_detection_job_properties"] = (
            aws_sdk_comprehend.types.dominant_language_detection_job_properties.deserialize_aws_json_1_1(
                data["DominantLanguageDetectionJobProperties"]
            )
        )
    return out
