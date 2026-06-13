"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#UpdateEnrollmentStatusResponse``."""

from typing import TypedDict

from typing_extensions import NotRequired


class UpdateEnrollmentStatusResponse(TypedDict):
    status: NotRequired["str"]
    """<p>The enrollment status of the account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnrollmentStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnrollmentStatusResponse:
    out: UpdateEnrollmentStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
