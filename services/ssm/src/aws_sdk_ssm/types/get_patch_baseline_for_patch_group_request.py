"""Generated from Smithy shape ``com.amazonaws.ssm#GetPatchBaselineForPatchGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.operating_system
    import aws_sdk_ssm.types.patch_group


class GetPatchBaselineForPatchGroupRequest(TypedDict, closed=True):
    patch_group: "aws_sdk_ssm.types.patch_group.PatchGroup"
    """<p>The name of the patch group whose patch baseline should be retrieved.</p>"""
    operating_system: NotRequired["aws_sdk_ssm.types.operating_system.OperatingSystem"]
    """<p>Returns the operating system rule specified for patch groups using the patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPatchBaselineForPatchGroupRequest) -> dict:
    out: dict = {}
    out["PatchGroup"] = value["patch_group"]
    if "operating_system" in value:
        import aws_sdk_ssm.types.operating_system

        out["OperatingSystem"] = (
            aws_sdk_ssm.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPatchBaselineForPatchGroupRequest:
    out: GetPatchBaselineForPatchGroupRequest = {}  # type: ignore[typeddict-item]
    if "PatchGroup" in data:
        out["patch_group"] = data["PatchGroup"]
    else:
        raise DeserializationError(
            "GetPatchBaselineForPatchGroupRequest.patch_group required"
        )
    if "OperatingSystem" in data:
        import aws_sdk_ssm.types.operating_system

        out["operating_system"] = (
            aws_sdk_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    return out
