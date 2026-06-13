"""Generated from Smithy shape ``com.amazonaws.drs#JobLogEventData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.conversion_properties
    import aws_sdk_drs.types.ec2_instance_id
    import aws_sdk_drs.types.event_resource_data
    import aws_sdk_drs.types.job_event_attempt_count
    import aws_sdk_drs.types.large_bounded_string
    import aws_sdk_drs.types.source_server_id


class JobLogEventData(TypedDict):
    source_server_id: NotRequired["aws_sdk_drs.types.source_server_id.SourceServerID"]
    """<p>The ID of a Source Server.</p>"""
    conversion_server_id: NotRequired["aws_sdk_drs.types.ec2_instance_id.EC2InstanceID"]
    """<p>The ID of a conversion server.</p>"""
    target_instance_id: NotRequired["aws_sdk_drs.types.ec2_instance_id.EC2InstanceID"]
    """<p>The ID of a Recovery Instance.</p>"""
    raw_error: NotRequired["aws_sdk_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>A string representing a job error.</p>"""
    conversion_properties: NotRequired[
        "aws_sdk_drs.types.conversion_properties.ConversionProperties"
    ]
    """<p>Properties of a conversion job</p>"""
    event_resource_data: NotRequired[
        "aws_sdk_drs.types.event_resource_data.EventResourceData"
    ]
    """<p>Properties of resource related to a job event.</p>"""
    attempt_count: "aws_sdk_drs.types.job_event_attempt_count.JobEventAttemptCount"
    """<p>Retries for this operation.</p>"""
    max_attempts_count: "aws_sdk_drs.types.job_event_attempt_count.JobEventAttemptCount"
    """<p>The maximum number of retries that will be attempted if this operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobLogEventData) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "conversion_server_id" in value:
        out["conversionServerID"] = value["conversion_server_id"]
    if "target_instance_id" in value:
        out["targetInstanceID"] = value["target_instance_id"]
    if "raw_error" in value:
        out["rawError"] = value["raw_error"]
    if "conversion_properties" in value:
        import aws_sdk_drs.types.conversion_properties

        out["conversionProperties"] = (
            aws_sdk_drs.types.conversion_properties.serialize_json(
                value["conversion_properties"]
            )
        )
    if "event_resource_data" in value:
        import aws_sdk_drs.types.event_resource_data

        out["eventResourceData"] = aws_sdk_drs.types.event_resource_data.serialize_json(
            value["event_resource_data"]
        )
    out["attemptCount"] = value.get("attempt_count", 0)
    out["maxAttemptsCount"] = value.get("max_attempts_count", 0)
    return out


def deserialize_json(data: dict) -> JobLogEventData:
    out: JobLogEventData = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    if "conversionServerID" in data:
        out["conversion_server_id"] = data["conversionServerID"]
    if "targetInstanceID" in data:
        out["target_instance_id"] = data["targetInstanceID"]
    if "rawError" in data:
        out["raw_error"] = data["rawError"]
    if "conversionProperties" in data:
        import aws_sdk_drs.types.conversion_properties

        out["conversion_properties"] = (
            aws_sdk_drs.types.conversion_properties.deserialize_json(
                data["conversionProperties"]
            )
        )
    if "eventResourceData" in data:
        import aws_sdk_drs.types.event_resource_data

        out["event_resource_data"] = (
            aws_sdk_drs.types.event_resource_data.deserialize_json(
                data["eventResourceData"]
            )
        )
    if "attemptCount" in data:
        out["attempt_count"] = data["attemptCount"]
    else:
        out["attempt_count"] = 0
    if "maxAttemptsCount" in data:
        out["max_attempts_count"] = data["maxAttemptsCount"]
    else:
        out["max_attempts_count"] = 0
    return out
