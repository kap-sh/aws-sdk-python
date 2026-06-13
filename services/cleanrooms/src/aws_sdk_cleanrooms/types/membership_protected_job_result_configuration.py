"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipProtectedJobResultConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_protected_job_output_configuration
    import aws_sdk_cleanrooms.types.role_arn


class MembershipProtectedJobResultConfiguration(TypedDict):
    output_configuration: "aws_sdk_cleanrooms.types.membership_protected_job_output_configuration.MembershipProtectedJobOutputConfiguration"
    """<p> The output configuration for a protected job result.</p>"""
    role_arn: "aws_sdk_cleanrooms.types.role_arn.RoleArn"
    """<p>The unique ARN for an IAM role that is used by Clean Rooms to write protected job results to the result location, given by the member who can receive results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipProtectedJobResultConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.membership_protected_job_output_configuration

    out["outputConfiguration"] = (
        aws_sdk_cleanrooms.types.membership_protected_job_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> MembershipProtectedJobResultConfiguration:
    out: MembershipProtectedJobResultConfiguration = {}  # type: ignore[typeddict-item]
    if "outputConfiguration" in data:
        import aws_sdk_cleanrooms.types.membership_protected_job_output_configuration

        out["output_configuration"] = (
            aws_sdk_cleanrooms.types.membership_protected_job_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "MembershipProtectedJobResultConfiguration.output_configuration required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "MembershipProtectedJobResultConfiguration.role_arn required"
        )
    return out
