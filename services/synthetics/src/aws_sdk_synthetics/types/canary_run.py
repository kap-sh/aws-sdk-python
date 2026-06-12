"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRun``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.browser_type
    import aws_sdk_synthetics.types.canary_dry_run_config_output
    import aws_sdk_synthetics.types.canary_name
    import aws_sdk_synthetics.types.canary_run_status
    import aws_sdk_synthetics.types.canary_run_timeline
    import aws_sdk_synthetics.types.retry_attempt
    import aws_sdk_synthetics.types.string
    import aws_sdk_synthetics.types.uuid


class CanaryRun(TypedDict):
    id: NotRequired["aws_sdk_synthetics.types.uuid.UUID"]
    """<p>A unique ID that identifies this canary run.</p>"""
    scheduled_run_id: NotRequired["aws_sdk_synthetics.types.uuid.UUID"]
    """<p>The ID of the scheduled canary run.</p>"""
    retry_attempt: NotRequired["aws_sdk_synthetics.types.retry_attempt.RetryAttempt"]
    """<p>The count in number of the retry attempt.</p>"""
    name: NotRequired["aws_sdk_synthetics.types.canary_name.CanaryName"]
    """<p>The name of the canary.</p>"""
    status: NotRequired["aws_sdk_synthetics.types.canary_run_status.CanaryRunStatus"]
    """<p>The status of this run.</p>"""
    timeline: NotRequired[
        "aws_sdk_synthetics.types.canary_run_timeline.CanaryRunTimeline"
    ]
    """<p>A structure that contains the start and end times of this run.</p>"""
    artifact_s3_location: NotRequired["aws_sdk_synthetics.types.string.String"]
    """<p>The location where the canary stored artifacts from the run. Artifacts include the log file, screenshots, and HAR files.</p>"""
    dry_run_config: NotRequired[
        "aws_sdk_synthetics.types.canary_dry_run_config_output.CanaryDryRunConfigOutput"
    ]
    """<p>Returns the dry run configurations for a canary.</p>"""
    browser_type: NotRequired["aws_sdk_synthetics.types.browser_type.BrowserType"]
    """<p>The browser type associated with this canary run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRun) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "scheduled_run_id" in value:
        out["ScheduledRunId"] = value["scheduled_run_id"]
    if "retry_attempt" in value:
        out["RetryAttempt"] = value["retry_attempt"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_synthetics.types.canary_run_status

        out["Status"] = aws_sdk_synthetics.types.canary_run_status.serialize_json(
            value["status"]
        )
    if "timeline" in value:
        import aws_sdk_synthetics.types.canary_run_timeline

        out["Timeline"] = aws_sdk_synthetics.types.canary_run_timeline.serialize_json(
            value["timeline"]
        )
    if "artifact_s3_location" in value:
        out["ArtifactS3Location"] = value["artifact_s3_location"]
    if "dry_run_config" in value:
        import aws_sdk_synthetics.types.canary_dry_run_config_output

        out["DryRunConfig"] = (
            aws_sdk_synthetics.types.canary_dry_run_config_output.serialize_json(
                value["dry_run_config"]
            )
        )
    if "browser_type" in value:
        import aws_sdk_synthetics.types.browser_type

        out["BrowserType"] = aws_sdk_synthetics.types.browser_type.serialize_json(
            value["browser_type"]
        )
    return out


def deserialize_json(data: dict) -> CanaryRun:
    out: CanaryRun = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ScheduledRunId" in data:
        out["scheduled_run_id"] = data["ScheduledRunId"]
    if "RetryAttempt" in data:
        out["retry_attempt"] = data["RetryAttempt"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_synthetics.types.canary_run_status

        out["status"] = aws_sdk_synthetics.types.canary_run_status.deserialize_json(
            data["Status"]
        )
    if "Timeline" in data:
        import aws_sdk_synthetics.types.canary_run_timeline

        out["timeline"] = aws_sdk_synthetics.types.canary_run_timeline.deserialize_json(
            data["Timeline"]
        )
    if "ArtifactS3Location" in data:
        out["artifact_s3_location"] = data["ArtifactS3Location"]
    if "DryRunConfig" in data:
        import aws_sdk_synthetics.types.canary_dry_run_config_output

        out["dry_run_config"] = (
            aws_sdk_synthetics.types.canary_dry_run_config_output.deserialize_json(
                data["DryRunConfig"]
            )
        )
    if "BrowserType" in data:
        import aws_sdk_synthetics.types.browser_type

        out["browser_type"] = aws_sdk_synthetics.types.browser_type.deserialize_json(
            data["BrowserType"]
        )
    return out
