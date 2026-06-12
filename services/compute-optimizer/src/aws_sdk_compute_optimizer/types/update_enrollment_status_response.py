"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UpdateEnrollmentStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.status
    import aws_sdk_compute_optimizer.types.status_reason


class UpdateEnrollmentStatusResponse(TypedDict):
    status: NotRequired["aws_sdk_compute_optimizer.types.status.Status"]
    """<p>The enrollment status of the account.</p>"""
    status_reason: NotRequired[
        "aws_sdk_compute_optimizer.types.status_reason.StatusReason"
    ]
    """<p>The reason for the enrollment status of the account. For example, an account might show a status of <code>Pending</code> because member accounts of an organization require more time to be enrolled in the service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnrollmentStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_compute_optimizer.types.status

        out["status"] = aws_sdk_compute_optimizer.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnrollmentStatusResponse:
    out: UpdateEnrollmentStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_compute_optimizer.types.status

        out["status"] = aws_sdk_compute_optimizer.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
