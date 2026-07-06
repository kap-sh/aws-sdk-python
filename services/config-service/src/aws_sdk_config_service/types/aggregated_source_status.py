"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatedSourceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregated_source_status_type
    import aws_sdk_config_service.types.aggregated_source_type
    import aws_sdk_config_service.types.aws_region
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.string


class AggregatedSourceStatus(TypedDict, closed=True):
    source_id: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The source account ID or an organization.</p>"""
    source_type: NotRequired[
        "aws_sdk_config_service.types.aggregated_source_type.AggregatedSourceType"
    ]
    """<p>The source account or an organization.</p>"""
    aws_region: NotRequired["aws_sdk_config_service.types.aws_region.AwsRegion"]
    """<p>The region authorized to collect aggregated data.</p>"""
    last_update_status: NotRequired[
        "aws_sdk_config_service.types.aggregated_source_status_type.AggregatedSourceStatusType"
    ]
    """<p>Filters the last updated status type.</p> <ul> <li> <p>Valid value FAILED indicates errors while moving data.</p> </li> <li> <p>Valid value SUCCEEDED indicates the data was successfully moved.</p> </li> <li> <p>Valid value OUTDATED indicates the data is not the most recent.</p> </li> </ul>"""
    last_update_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time of the last update.</p>"""
    last_error_code: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The error code that Config returned when the source account aggregation last failed.</p>"""
    last_error_message: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The message indicating that the source account aggregation failed due to an error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedSourceStatus) -> dict:
    out: dict = {}
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    if "source_type" in value:
        import aws_sdk_config_service.types.aggregated_source_type

        out["SourceType"] = (
            aws_sdk_config_service.types.aggregated_source_type.serialize_aws_json_1_1(
                value["source_type"]
            )
        )
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    if "last_update_status" in value:
        import aws_sdk_config_service.types.aggregated_source_status_type

        out["LastUpdateStatus"] = (
            aws_sdk_config_service.types.aggregated_source_status_type.serialize_aws_json_1_1(
                value["last_update_status"]
            )
        )
    if "last_update_time" in value:
        import aws_sdk_config_service.types.date

        out["LastUpdateTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_update_time"]
            )
        )
    if "last_error_code" in value:
        out["LastErrorCode"] = value["last_error_code"]
    if "last_error_message" in value:
        out["LastErrorMessage"] = value["last_error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregatedSourceStatus:
    out: AggregatedSourceStatus = {}  # type: ignore[typeddict-item]
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    if "SourceType" in data:
        import aws_sdk_config_service.types.aggregated_source_type

        out["source_type"] = (
            aws_sdk_config_service.types.aggregated_source_type.deserialize_aws_json_1_1(
                data["SourceType"]
            )
        )
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    if "LastUpdateStatus" in data:
        import aws_sdk_config_service.types.aggregated_source_status_type

        out["last_update_status"] = (
            aws_sdk_config_service.types.aggregated_source_status_type.deserialize_aws_json_1_1(
                data["LastUpdateStatus"]
            )
        )
    if "LastUpdateTime" in data:
        import aws_sdk_config_service.types.date

        out["last_update_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    if "LastErrorCode" in data:
        out["last_error_code"] = data["LastErrorCode"]
    if "LastErrorMessage" in data:
        out["last_error_message"] = data["LastErrorMessage"]
    return out
