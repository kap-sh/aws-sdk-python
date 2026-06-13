"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateProtectedJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.protected_job_identifier
    import aws_sdk_cleanrooms.types.target_protected_job_status


class UpdateProtectedJobInput(TypedDict):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a member of a protected job instance.</p>"""
    protected_job_identifier: (
        "aws_sdk_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier"
    )
    """<p> The identifier of the protected job to update.</p>"""
    target_status: (
        "aws_sdk_cleanrooms.types.target_protected_job_status.TargetProtectedJobStatus"
    )
    """<p>The target status of a protected job. Used to update the execution status of a currently running job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProtectedJobInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.target_protected_job_status

    out["targetStatus"] = (
        aws_sdk_cleanrooms.types.target_protected_job_status.serialize_json(
            value["target_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateProtectedJobInput:
    out: UpdateProtectedJobInput = {}  # type: ignore[typeddict-item]
    if "targetStatus" in data:
        import aws_sdk_cleanrooms.types.target_protected_job_status

        out["target_status"] = (
            aws_sdk_cleanrooms.types.target_protected_job_status.deserialize_json(
                data["targetStatus"]
            )
        )
    else:
        raise DeserializationError("UpdateProtectedJobInput.target_status required")
    return out
