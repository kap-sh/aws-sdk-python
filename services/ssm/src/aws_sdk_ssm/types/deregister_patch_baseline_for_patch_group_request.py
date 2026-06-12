"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterPatchBaselineForPatchGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.baseline_id
    import aws_sdk_ssm.types.patch_group


class DeregisterPatchBaselineForPatchGroupRequest(TypedDict):
    baseline_id: "aws_sdk_ssm.types.baseline_id.BaselineId"
    """<p>The ID of the patch baseline to deregister the patch group from.</p>"""
    patch_group: "aws_sdk_ssm.types.patch_group.PatchGroup"
    """<p>The name of the patch group that should be deregistered from the patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterPatchBaselineForPatchGroupRequest) -> dict:
    out: dict = {}
    out["BaselineId"] = value["baseline_id"]
    out["PatchGroup"] = value["patch_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterPatchBaselineForPatchGroupRequest:
    out: DeregisterPatchBaselineForPatchGroupRequest = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    else:
        raise DeserializationError(
            "DeregisterPatchBaselineForPatchGroupRequest.baseline_id required"
        )
    if "PatchGroup" in data:
        out["patch_group"] = data["PatchGroup"]
    else:
        raise DeserializationError(
            "DeregisterPatchBaselineForPatchGroupRequest.patch_group required"
        )
    return out
