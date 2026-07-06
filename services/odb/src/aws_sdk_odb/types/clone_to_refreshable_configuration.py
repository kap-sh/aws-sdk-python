"""Generated from Smithy shape ``com.amazonaws.odb#CloneToRefreshableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.clone_type
    import aws_sdk_odb.types.open_mode
    import aws_sdk_odb.types.refreshable_mode
    import aws_sdk_odb.types.resource_id_or_arn


class CloneToRefreshableConfiguration(TypedDict, closed=True):
    source_autonomous_database_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the source Autonomous Database to create the refreshable clone from.</p>"""
    refreshable_mode: NotRequired["aws_sdk_odb.types.refreshable_mode.RefreshableMode"]
    """<p>The refresh mode of the refreshable clone, either automatic or manual.</p>"""
    auto_refresh_frequency_in_seconds: NotRequired["int"]
    """<p>The frequency, in seconds, at which the refreshable clone is automatically refreshed.</p>"""
    auto_refresh_point_lag_in_seconds: NotRequired["int"]
    """<p>The time lag, in seconds, between the refreshable clone and its source database.</p>"""
    time_of_auto_refresh_start: NotRequired["datetime.datetime"]
    """<p>The date and time at which the automatic refresh of the refreshable clone starts.</p>"""
    open_mode: NotRequired["aws_sdk_odb.types.open_mode.OpenMode"]
    """<p>The mode in which to open the refreshable clone, either read-only or read/write.</p>"""
    clone_type: NotRequired["aws_sdk_odb.types.clone_type.CloneType"]
    """<p>The type of clone to create.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloneToRefreshableConfiguration) -> dict:
    out: dict = {}
    out["sourceAutonomousDatabaseId"] = value["source_autonomous_database_id"]
    if "refreshable_mode" in value:
        import aws_sdk_odb.types.refreshable_mode

        out["refreshableMode"] = (
            aws_sdk_odb.types.refreshable_mode.serialize_aws_json_1_0(
                value["refreshable_mode"]
            )
        )
    if "auto_refresh_frequency_in_seconds" in value:
        out["autoRefreshFrequencyInSeconds"] = value[
            "auto_refresh_frequency_in_seconds"
        ]
    if "auto_refresh_point_lag_in_seconds" in value:
        out["autoRefreshPointLagInSeconds"] = value["auto_refresh_point_lag_in_seconds"]
    if "time_of_auto_refresh_start" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfAutoRefreshStart"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_auto_refresh_start"]
            )
        )
    if "open_mode" in value:
        import aws_sdk_odb.types.open_mode

        out["openMode"] = aws_sdk_odb.types.open_mode.serialize_aws_json_1_0(
            value["open_mode"]
        )
    if "clone_type" in value:
        import aws_sdk_odb.types.clone_type

        out["cloneType"] = aws_sdk_odb.types.clone_type.serialize_aws_json_1_0(
            value["clone_type"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CloneToRefreshableConfiguration:
    out: CloneToRefreshableConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceAutonomousDatabaseId" in data:
        out["source_autonomous_database_id"] = data["sourceAutonomousDatabaseId"]
    else:
        raise DeserializationError(
            "CloneToRefreshableConfiguration.source_autonomous_database_id required"
        )
    if "refreshableMode" in data:
        import aws_sdk_odb.types.refreshable_mode

        out["refreshable_mode"] = (
            aws_sdk_odb.types.refreshable_mode.deserialize_aws_json_1_0(
                data["refreshableMode"]
            )
        )
    if "autoRefreshFrequencyInSeconds" in data:
        out["auto_refresh_frequency_in_seconds"] = data["autoRefreshFrequencyInSeconds"]
    if "autoRefreshPointLagInSeconds" in data:
        out["auto_refresh_point_lag_in_seconds"] = data["autoRefreshPointLagInSeconds"]
    if "timeOfAutoRefreshStart" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_auto_refresh_start"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfAutoRefreshStart"]
            )
        )
    if "openMode" in data:
        import aws_sdk_odb.types.open_mode

        out["open_mode"] = aws_sdk_odb.types.open_mode.deserialize_aws_json_1_0(
            data["openMode"]
        )
    if "cloneType" in data:
        import aws_sdk_odb.types.clone_type

        out["clone_type"] = aws_sdk_odb.types.clone_type.deserialize_aws_json_1_0(
            data["cloneType"]
        )
    return out
