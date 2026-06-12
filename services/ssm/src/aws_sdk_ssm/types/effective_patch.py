"""Generated from Smithy shape ``com.amazonaws.ssm#EffectivePatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch
    import aws_sdk_ssm.types.patch_status


class EffectivePatch(TypedDict):
    patch: NotRequired["aws_sdk_ssm.types.patch.Patch"]
    """<p>Provides metadata for a patch, including information such as the KB ID, severity, classification and a URL for where more information can be obtained about the patch.</p>"""
    patch_status: NotRequired["aws_sdk_ssm.types.patch_status.PatchStatus"]
    """<p>The status of the patch in a patch baseline. This includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectivePatch) -> dict:
    out: dict = {}
    if "patch" in value:
        import aws_sdk_ssm.types.patch

        out["Patch"] = aws_sdk_ssm.types.patch.serialize_aws_json_1_1(value["patch"])
    if "patch_status" in value:
        import aws_sdk_ssm.types.patch_status

        out["PatchStatus"] = aws_sdk_ssm.types.patch_status.serialize_aws_json_1_1(
            value["patch_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EffectivePatch:
    out: EffectivePatch = {}  # type: ignore[typeddict-item]
    if "Patch" in data:
        import aws_sdk_ssm.types.patch

        out["patch"] = aws_sdk_ssm.types.patch.deserialize_aws_json_1_1(data["Patch"])
    if "PatchStatus" in data:
        import aws_sdk_ssm.types.patch_status

        out["patch_status"] = aws_sdk_ssm.types.patch_status.deserialize_aws_json_1_1(
            data["PatchStatus"]
        )
    return out
