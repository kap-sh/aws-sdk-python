"""Generated from Smithy shape ``com.amazonaws.glue#StatisticAnnotation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.timestamped_inclusion_annotation


class StatisticAnnotation(TypedDict, closed=True):
    profile_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Profile ID.</p>"""
    statistic_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Statistic ID.</p>"""
    statistic_recorded_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The timestamp when the annotated statistic was recorded.</p>"""
    inclusion_annotation: NotRequired[
        "aws_sdk_glue.types.timestamped_inclusion_annotation.TimestampedInclusionAnnotation"
    ]
    """<p>The inclusion annotation applied to the statistic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticAnnotation) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    if "statistic_recorded_on" in value:
        import aws_sdk_glue.types.timestamp

        out["StatisticRecordedOn"] = (
            aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
                value["statistic_recorded_on"]
            )
        )
    if "inclusion_annotation" in value:
        import aws_sdk_glue.types.timestamped_inclusion_annotation

        out["InclusionAnnotation"] = (
            aws_sdk_glue.types.timestamped_inclusion_annotation.serialize_aws_json_1_1(
                value["inclusion_annotation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatisticAnnotation:
    out: StatisticAnnotation = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "StatisticId" in data:
        out["statistic_id"] = data["StatisticId"]
    if "StatisticRecordedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["statistic_recorded_on"] = (
            aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
                data["StatisticRecordedOn"]
            )
        )
    if "InclusionAnnotation" in data:
        import aws_sdk_glue.types.timestamped_inclusion_annotation

        out["inclusion_annotation"] = (
            aws_sdk_glue.types.timestamped_inclusion_annotation.deserialize_aws_json_1_1(
                data["InclusionAnnotation"]
            )
        )
    return out
