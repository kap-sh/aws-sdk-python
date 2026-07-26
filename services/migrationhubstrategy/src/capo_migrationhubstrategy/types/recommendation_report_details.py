"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#RecommendationReportDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.recommendation_report_status
    import capo_migrationhubstrategy.types.recommendation_report_status_message
    import capo_migrationhubstrategy.types.recommendation_report_time_stamp
    import capo_migrationhubstrategy.types.s3_keys
    import capo_migrationhubstrategy.types.string


class RecommendationReportDetails(TypedDict, closed=True):
    status: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_report_status.RecommendationReportStatus"
    ]
    """<p> The status of the recommendation report generation task. </p>"""
    status_message: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_report_status_message.RecommendationReportStatusMessage"
    ]
    """<p> The status message for recommendation report generation. </p>"""
    start_time: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_report_time_stamp.RecommendationReportTimeStamp"
    ]
    """<p> The time that the recommendation report generation task starts. </p>"""
    completion_time: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_report_time_stamp.RecommendationReportTimeStamp"
    ]
    """<p> The time that the recommendation report generation task completes. </p>"""
    s3_bucket: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> The S3 bucket where the report file is located. </p>"""
    s3_keys: NotRequired["capo_migrationhubstrategy.types.s3_keys.S3Keys"]
    """<p> The Amazon S3 key name of the report file. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationReportDetails) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "start_time" in value:
        import capo_migrationhubstrategy.types.recommendation_report_time_stamp

        out["startTime"] = (
            capo_migrationhubstrategy.types.recommendation_report_time_stamp.serialize_json(
                value["start_time"]
            )
        )
    if "completion_time" in value:
        import capo_migrationhubstrategy.types.recommendation_report_time_stamp

        out["completionTime"] = (
            capo_migrationhubstrategy.types.recommendation_report_time_stamp.serialize_json(
                value["completion_time"]
            )
        )
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3_keys" in value:
        import capo_migrationhubstrategy.types.s3_keys

        out["s3Keys"] = capo_migrationhubstrategy.types.s3_keys.serialize_json(
            value["s3_keys"]
        )
    return out


def deserialize_json(data: dict) -> RecommendationReportDetails:
    out: RecommendationReportDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "startTime" in data:
        import capo_migrationhubstrategy.types.recommendation_report_time_stamp

        out["start_time"] = (
            capo_migrationhubstrategy.types.recommendation_report_time_stamp.deserialize_json(
                data["startTime"]
            )
        )
    if "completionTime" in data:
        import capo_migrationhubstrategy.types.recommendation_report_time_stamp

        out["completion_time"] = (
            capo_migrationhubstrategy.types.recommendation_report_time_stamp.deserialize_json(
                data["completionTime"]
            )
        )
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    if "s3Keys" in data:
        import capo_migrationhubstrategy.types.s3_keys

        out["s3_keys"] = capo_migrationhubstrategy.types.s3_keys.deserialize_json(
            data["s3Keys"]
        )
    return out
