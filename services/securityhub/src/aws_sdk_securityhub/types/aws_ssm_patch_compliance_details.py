"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSsmPatchComplianceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ssm_patch


class AwsSsmPatchComplianceDetails(TypedDict, closed=True):
    patch: NotRequired["aws_sdk_securityhub.types.aws_ssm_patch.AwsSsmPatch"]
    """<p>Information about the status of a patch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSsmPatchComplianceDetails) -> dict:
    out: dict = {}
    if "patch" in value:
        import aws_sdk_securityhub.types.aws_ssm_patch

        out["Patch"] = aws_sdk_securityhub.types.aws_ssm_patch.serialize_json(
            value["patch"]
        )
    return out


def deserialize_json(data: dict) -> AwsSsmPatchComplianceDetails:
    out: AwsSsmPatchComplianceDetails = {}  # type: ignore[typeddict-item]
    if "Patch" in data:
        import aws_sdk_securityhub.types.aws_ssm_patch

        out["patch"] = aws_sdk_securityhub.types.aws_ssm_patch.deserialize_json(
            data["Patch"]
        )
    return out
