"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterDefaultPatchBaselineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.baseline_id


class RegisterDefaultPatchBaselineRequest(TypedDict):
    baseline_id: "aws_sdk_ssm.types.baseline_id.BaselineId"
    """<p>The ID of the patch baseline that should be the default patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDefaultPatchBaselineRequest) -> dict:
    out: dict = {}
    out["BaselineId"] = value["baseline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDefaultPatchBaselineRequest:
    out: RegisterDefaultPatchBaselineRequest = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    else:
        raise DeserializationError(
            "RegisterDefaultPatchBaselineRequest.baseline_id required"
        )
    return out
