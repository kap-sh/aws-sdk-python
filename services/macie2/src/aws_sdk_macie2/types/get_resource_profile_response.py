"""Generated from Smithy shape ``com.amazonaws.macie2#GetResourceProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.resource_statistics


class GetResourceProfileResponse(TypedDict, closed=True):
    profile_updated_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently recalculated sensitive data discovery statistics and details for the bucket. If the bucket's sensitivity score is calculated automatically, this includes the score.</p>"""
    sensitivity_score: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The current sensitivity score for the bucket, ranging from -1 (classification error) to 100 (sensitive). By default, this score is calculated automatically based on the amount of data that Amazon Macie has analyzed in the bucket and the amount of sensitive data that Macie has found in the bucket.</p>"""
    sensitivity_score_overridden: NotRequired[
        "aws_sdk_macie2.types.__boolean.__boolean"
    ]
    """<p>Specifies whether the bucket's current sensitivity score was set manually. If this value is true, the score was manually changed to 100. If this value is false, the score was calculated automatically by Amazon Macie.</p>"""
    statistics: NotRequired[
        "aws_sdk_macie2.types.resource_statistics.ResourceStatistics"
    ]
    """<p>The sensitive data discovery statistics for the bucket. The statistics capture the results of automated sensitive data discovery activities that Amazon Macie has performed for the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceProfileResponse) -> dict:
    out: dict = {}
    if "profile_updated_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["profileUpdatedAt"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
                value["profile_updated_at"]
            )
        )
    if "sensitivity_score" in value:
        out["sensitivityScore"] = value["sensitivity_score"]
    if "sensitivity_score_overridden" in value:
        out["sensitivityScoreOverridden"] = value["sensitivity_score_overridden"]
    if "statistics" in value:
        import aws_sdk_macie2.types.resource_statistics

        out["statistics"] = aws_sdk_macie2.types.resource_statistics.serialize_json(
            value["statistics"]
        )
    return out


def deserialize_json(data: dict) -> GetResourceProfileResponse:
    out: GetResourceProfileResponse = {}  # type: ignore[typeddict-item]
    if "profileUpdatedAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["profile_updated_at"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["profileUpdatedAt"]
            )
        )
    if "sensitivityScore" in data:
        out["sensitivity_score"] = data["sensitivityScore"]
    if "sensitivityScoreOverridden" in data:
        out["sensitivity_score_overridden"] = data["sensitivityScoreOverridden"]
    if "statistics" in data:
        import aws_sdk_macie2.types.resource_statistics

        out["statistics"] = aws_sdk_macie2.types.resource_statistics.deserialize_json(
            data["statistics"]
        )
    return out
