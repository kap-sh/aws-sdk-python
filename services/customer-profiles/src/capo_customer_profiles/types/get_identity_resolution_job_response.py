"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetIdentityResolutionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.auto_merging
    import capo_customer_profiles.types.exporting_location
    import capo_customer_profiles.types.identity_resolution_job_status
    import capo_customer_profiles.types.job_stats
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string_to2048
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.uuid


class GetIdentityResolutionJobResponse(TypedDict, closed=True):
    domain_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The unique name of the domain.</p>"""
    job_id: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>The unique identifier of the Identity Resolution Job.</p>"""
    status: NotRequired[
        "capo_customer_profiles.types.identity_resolution_job_status.IdentityResolutionJobStatus"
    ]
    """<p>The status of the Identity Resolution Job.</p> <ul> <li> <p> <code>PENDING</code>: The Identity Resolution Job is scheduled but has not started yet. If you turn off the Identity Resolution feature in your domain, jobs in the <code>PENDING</code> state are deleted.</p> </li> <li> <p> <code>PREPROCESSING</code>: The Identity Resolution Job is loading your data.</p> </li> <li> <p> <code>FIND_MATCHING</code>: The Identity Resolution Job is using the machine learning model to identify profiles that belong to the same matching group.</p> </li> <li> <p> <code>MERGING</code>: The Identity Resolution Job is merging duplicate profiles.</p> </li> <li> <p> <code>COMPLETED</code>: The Identity Resolution Job completed successfully.</p> </li> <li> <p> <code>PARTIAL_SUCCESS</code>: There's a system error and not all of the data is merged. The Identity Resolution Job writes a message indicating the source of the problem.</p> </li> <li> <p> <code>FAILED</code>: The Identity Resolution Job did not merge any data. It writes a message indicating the source of the problem.</p> </li> </ul>"""
    message: NotRequired["capo_customer_profiles.types.string_to2048.stringTo2048"]
    """<p>The error messages that are generated when the Identity Resolution Job runs.</p>"""
    job_start_time: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the Identity Resolution Job was started or will be started.</p>"""
    job_end_time: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the Identity Resolution Job was completed.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the Identity Resolution Job was most recently edited.</p>"""
    job_expiration_time: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the Identity Resolution Job will expire.</p>"""
    auto_merging: NotRequired["capo_customer_profiles.types.auto_merging.AutoMerging"]
    """<p>Configuration settings for how to perform the auto-merging of profiles.</p>"""
    exporting_location: NotRequired[
        "capo_customer_profiles.types.exporting_location.ExportingLocation"
    ]
    """<p>The S3 location where the Identity Resolution Job writes result files.</p>"""
    job_stats: NotRequired["capo_customer_profiles.types.job_stats.JobStats"]
    """<p>Statistics about the Identity Resolution Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityResolutionJobResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "status" in value:
        import capo_customer_profiles.types.identity_resolution_job_status

        out["Status"] = (
            capo_customer_profiles.types.identity_resolution_job_status.serialize_json(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "job_start_time" in value:
        import capo_customer_profiles.types.timestamp

        out["JobStartTime"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["job_start_time"]
        )
    if "job_end_time" in value:
        import capo_customer_profiles.types.timestamp

        out["JobEndTime"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["job_end_time"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "job_expiration_time" in value:
        import capo_customer_profiles.types.timestamp

        out["JobExpirationTime"] = (
            capo_customer_profiles.types.timestamp.serialize_json(
                value["job_expiration_time"]
            )
        )
    if "auto_merging" in value:
        import capo_customer_profiles.types.auto_merging

        out["AutoMerging"] = capo_customer_profiles.types.auto_merging.serialize_json(
            value["auto_merging"]
        )
    if "exporting_location" in value:
        import capo_customer_profiles.types.exporting_location

        out["ExportingLocation"] = (
            capo_customer_profiles.types.exporting_location.serialize_json(
                value["exporting_location"]
            )
        )
    if "job_stats" in value:
        import capo_customer_profiles.types.job_stats

        out["JobStats"] = capo_customer_profiles.types.job_stats.serialize_json(
            value["job_stats"]
        )
    return out


def deserialize_json(data: dict) -> GetIdentityResolutionJobResponse:
    out: GetIdentityResolutionJobResponse = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Status" in data:
        import capo_customer_profiles.types.identity_resolution_job_status

        out["status"] = (
            capo_customer_profiles.types.identity_resolution_job_status.deserialize_json(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "JobStartTime" in data:
        import capo_customer_profiles.types.timestamp

        out["job_start_time"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["JobStartTime"]
        )
    if "JobEndTime" in data:
        import capo_customer_profiles.types.timestamp

        out["job_end_time"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["JobEndTime"]
        )
    if "LastUpdatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "JobExpirationTime" in data:
        import capo_customer_profiles.types.timestamp

        out["job_expiration_time"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["JobExpirationTime"]
            )
        )
    if "AutoMerging" in data:
        import capo_customer_profiles.types.auto_merging

        out["auto_merging"] = (
            capo_customer_profiles.types.auto_merging.deserialize_json(
                data["AutoMerging"]
            )
        )
    if "ExportingLocation" in data:
        import capo_customer_profiles.types.exporting_location

        out["exporting_location"] = (
            capo_customer_profiles.types.exporting_location.deserialize_json(
                data["ExportingLocation"]
            )
        )
    if "JobStats" in data:
        import capo_customer_profiles.types.job_stats

        out["job_stats"] = capo_customer_profiles.types.job_stats.deserialize_json(
            data["JobStats"]
        )
    return out
