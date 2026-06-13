"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.protected_job_compute_configuration
    import aws_sdk_cleanrooms.types.protected_job_error
    import aws_sdk_cleanrooms.types.protected_job_identifier
    import aws_sdk_cleanrooms.types.protected_job_parameters
    import aws_sdk_cleanrooms.types.protected_job_result
    import aws_sdk_cleanrooms.types.protected_job_result_configuration_output
    import aws_sdk_cleanrooms.types.protected_job_statistics
    import aws_sdk_cleanrooms.types.protected_job_status


class ProtectedJob(TypedDict):
    id: "aws_sdk_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier"
    """<p>The identifier for a protected job instance.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>he identifier for the membership.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The ARN of the membership.</p>"""
    create_time: "datetime.datetime"
    """<p> The creation time of the protected job.</p>"""
    job_parameters: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_parameters.ProtectedJobParameters"
    ]
    """<p> The job parameters for the protected job.</p>"""
    status: "aws_sdk_cleanrooms.types.protected_job_status.ProtectedJobStatus"
    """<p> The status of the protected job.</p>"""
    result_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_result_configuration_output.ProtectedJobResultConfigurationOutput"
    ]
    """<p>Contains any details needed to write the job results.</p>"""
    statistics: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_statistics.ProtectedJobStatistics"
    ]
    """<p> The statistics of the protected job.</p>"""
    result: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_result.ProtectedJobResult"
    ]
    """<p> The result of the protected job.</p>"""
    error: NotRequired["aws_sdk_cleanrooms.types.protected_job_error.ProtectedJobError"]
    """<p> The error from the protected job.</p>"""
    compute_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
    ]
    """<p>The compute configuration for the protected job.</p>"""
    job_compute_payer_account_id: NotRequired[
        "aws_sdk_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the job compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJob) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    if "job_parameters" in value:
        import aws_sdk_cleanrooms.types.protected_job_parameters

        out["jobParameters"] = (
            aws_sdk_cleanrooms.types.protected_job_parameters.serialize_json(
                value["job_parameters"]
            )
        )
    import aws_sdk_cleanrooms.types.protected_job_status

    out["status"] = aws_sdk_cleanrooms.types.protected_job_status.serialize_json(
        value["status"]
    )
    if "result_configuration" in value:
        import aws_sdk_cleanrooms.types.protected_job_result_configuration_output

        out["resultConfiguration"] = (
            aws_sdk_cleanrooms.types.protected_job_result_configuration_output.serialize_json(
                value["result_configuration"]
            )
        )
    if "statistics" in value:
        import aws_sdk_cleanrooms.types.protected_job_statistics

        out["statistics"] = (
            aws_sdk_cleanrooms.types.protected_job_statistics.serialize_json(
                value["statistics"]
            )
        )
    if "result" in value:
        import aws_sdk_cleanrooms.types.protected_job_result

        out["result"] = aws_sdk_cleanrooms.types.protected_job_result.serialize_json(
            value["result"]
        )
    if "error" in value:
        import aws_sdk_cleanrooms.types.protected_job_error

        out["error"] = aws_sdk_cleanrooms.types.protected_job_error.serialize_json(
            value["error"]
        )
    if "compute_configuration" in value:
        import aws_sdk_cleanrooms.types.protected_job_compute_configuration

        out["computeConfiguration"] = (
            aws_sdk_cleanrooms.types.protected_job_compute_configuration.serialize_json(
                value["compute_configuration"]
            )
        )
    if "job_compute_payer_account_id" in value:
        out["jobComputePayerAccountId"] = value["job_compute_payer_account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedJob:
    out: ProtectedJob = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ProtectedJob.id required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("ProtectedJob.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("ProtectedJob.membership_arn required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("ProtectedJob.create_time required")
    if "jobParameters" in data:
        import aws_sdk_cleanrooms.types.protected_job_parameters

        out["job_parameters"] = (
            aws_sdk_cleanrooms.types.protected_job_parameters.deserialize_json(
                data["jobParameters"]
            )
        )
    if "status" in data:
        import aws_sdk_cleanrooms.types.protected_job_status

        out["status"] = aws_sdk_cleanrooms.types.protected_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ProtectedJob.status required")
    if "resultConfiguration" in data:
        import aws_sdk_cleanrooms.types.protected_job_result_configuration_output

        out["result_configuration"] = (
            aws_sdk_cleanrooms.types.protected_job_result_configuration_output.deserialize_json(
                data["resultConfiguration"]
            )
        )
    if "statistics" in data:
        import aws_sdk_cleanrooms.types.protected_job_statistics

        out["statistics"] = (
            aws_sdk_cleanrooms.types.protected_job_statistics.deserialize_json(
                data["statistics"]
            )
        )
    if "result" in data:
        import aws_sdk_cleanrooms.types.protected_job_result

        out["result"] = aws_sdk_cleanrooms.types.protected_job_result.deserialize_json(
            data["result"]
        )
    if "error" in data:
        import aws_sdk_cleanrooms.types.protected_job_error

        out["error"] = aws_sdk_cleanrooms.types.protected_job_error.deserialize_json(
            data["error"]
        )
    if "computeConfiguration" in data:
        import aws_sdk_cleanrooms.types.protected_job_compute_configuration

        out["compute_configuration"] = (
            aws_sdk_cleanrooms.types.protected_job_compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if "jobComputePayerAccountId" in data:
        out["job_compute_payer_account_id"] = data["jobComputePayerAccountId"]
    return out
