"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IdentityResolutionJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.exporting_location
    import aws_sdk_customer_profiles.types.identity_resolution_job_status
    import aws_sdk_customer_profiles.types.job_stats
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string_to2048
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.uuid


class IdentityResolutionJob(TypedDict):
    domain_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The unique name of the domain.</p>"""
    job_id: NotRequired["aws_sdk_customer_profiles.types.uuid.uuid"]
    """<p>The unique identifier of the Identity Resolution Job.</p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.identity_resolution_job_status.IdentityResolutionJobStatus"
    ]
    """<p>The status of the Identity Resolution Job.</p> <ul> <li> <p> <code>PENDING</code>: The Identity Resolution Job is scheduled but has not started yet. If you turn off the Identity Resolution feature in your domain, jobs in the <code>PENDING</code> state are deleted.</p> </li> <li> <p> <code>PREPROCESSING</code>: The Identity Resolution Job is loading your data.</p> </li> <li> <p> <code>FIND_MATCHING</code>: The Identity Resolution Job is using the machine learning model to identify profiles that belong to the same matching group.</p> </li> <li> <p> <code>MERGING</code>: The Identity Resolution Job is merging duplicate profiles.</p> </li> <li> <p> <code>COMPLETED</code>: The Identity Resolution Job completed successfully.</p> </li> <li> <p> <code>PARTIAL_SUCCESS</code>: There's a system error and not all of the data is merged. The Identity Resolution Job writes a message indicating the source of the problem.</p> </li> <li> <p> <code>FAILED</code>: The Identity Resolution Job did not merge any data. It writes a message indicating the source of the problem.</p> </li> </ul>"""
    job_start_time: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the job was started or will be started.</p>"""
    job_end_time: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the job was completed.</p>"""
    job_stats: NotRequired["aws_sdk_customer_profiles.types.job_stats.JobStats"]
    """<p>Statistics about an Identity Resolution Job.</p>"""
    exporting_location: NotRequired[
        "aws_sdk_customer_profiles.types.exporting_location.ExportingLocation"
    ]
    """<p>The S3 location where the Identity Resolution Job writes result files.</p>"""
    message: NotRequired["aws_sdk_customer_profiles.types.string_to2048.stringTo2048"]
    """<p>The error messages that are generated when the Identity Resolution Job runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityResolutionJob) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "status" in value:
        import aws_sdk_customer_profiles.types.identity_resolution_job_status

        out["Status"] = (
            aws_sdk_customer_profiles.types.identity_resolution_job_status.serialize_json(
                value["status"]
            )
        )
    if "job_start_time" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["JobStartTime"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["job_start_time"]
        )
    if "job_end_time" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["JobEndTime"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["job_end_time"]
        )
    if "job_stats" in value:
        import aws_sdk_customer_profiles.types.job_stats

        out["JobStats"] = aws_sdk_customer_profiles.types.job_stats.serialize_json(
            value["job_stats"]
        )
    if "exporting_location" in value:
        import aws_sdk_customer_profiles.types.exporting_location

        out["ExportingLocation"] = (
            aws_sdk_customer_profiles.types.exporting_location.serialize_json(
                value["exporting_location"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IdentityResolutionJob:
    out: IdentityResolutionJob = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Status" in data:
        import aws_sdk_customer_profiles.types.identity_resolution_job_status

        out["status"] = (
            aws_sdk_customer_profiles.types.identity_resolution_job_status.deserialize_json(
                data["Status"]
            )
        )
    if "JobStartTime" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["job_start_time"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["JobStartTime"]
            )
        )
    if "JobEndTime" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["job_end_time"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["JobEndTime"]
            )
        )
    if "JobStats" in data:
        import aws_sdk_customer_profiles.types.job_stats

        out["job_stats"] = aws_sdk_customer_profiles.types.job_stats.deserialize_json(
            data["JobStats"]
        )
    if "ExportingLocation" in data:
        import aws_sdk_customer_profiles.types.exporting_location

        out["exporting_location"] = (
            aws_sdk_customer_profiles.types.exporting_location.deserialize_json(
                data["ExportingLocation"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
