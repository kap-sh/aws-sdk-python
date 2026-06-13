"""Generated from Smithy shape ``com.amazonaws.cleanrooms#StartProtectedJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.protected_job_compute_configuration
    import aws_sdk_cleanrooms.types.protected_job_parameters
    import aws_sdk_cleanrooms.types.protected_job_result_configuration_input
    import aws_sdk_cleanrooms.types.protected_job_type


class StartProtectedJobInput(TypedDict):
    type: "aws_sdk_cleanrooms.types.protected_job_type.ProtectedJobType"
    """<p> The type of protected job to start.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership to run this job against. Currently accepts a membership ID.</p>"""
    job_parameters: (
        "aws_sdk_cleanrooms.types.protected_job_parameters.ProtectedJobParameters"
    )
    """<p> The job parameters.</p>"""
    result_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_result_configuration_input.ProtectedJobResultConfigurationInput"
    ]
    """<p>The details needed to write the job results.</p>"""
    compute_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
    ]
    """<p>The compute configuration for the protected job.</p>"""
    job_compute_payer_account_id: NotRequired[
        "aws_sdk_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the job compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProtectedJobInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_job_type

    out["type"] = aws_sdk_cleanrooms.types.protected_job_type.serialize_json(
        value["type"]
    )
    import aws_sdk_cleanrooms.types.protected_job_parameters

    out["jobParameters"] = (
        aws_sdk_cleanrooms.types.protected_job_parameters.serialize_json(
            value["job_parameters"]
        )
    )
    if "result_configuration" in value:
        import aws_sdk_cleanrooms.types.protected_job_result_configuration_input

        out["resultConfiguration"] = (
            aws_sdk_cleanrooms.types.protected_job_result_configuration_input.serialize_json(
                value["result_configuration"]
            )
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


def deserialize_json(data: dict) -> StartProtectedJobInput:
    out: StartProtectedJobInput = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_cleanrooms.types.protected_job_type

        out["type"] = aws_sdk_cleanrooms.types.protected_job_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("StartProtectedJobInput.type required")
    if "jobParameters" in data:
        import aws_sdk_cleanrooms.types.protected_job_parameters

        out["job_parameters"] = (
            aws_sdk_cleanrooms.types.protected_job_parameters.deserialize_json(
                data["jobParameters"]
            )
        )
    else:
        raise DeserializationError("StartProtectedJobInput.job_parameters required")
    if "resultConfiguration" in data:
        import aws_sdk_cleanrooms.types.protected_job_result_configuration_input

        out["result_configuration"] = (
            aws_sdk_cleanrooms.types.protected_job_result_configuration_input.deserialize_json(
                data["resultConfiguration"]
            )
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
