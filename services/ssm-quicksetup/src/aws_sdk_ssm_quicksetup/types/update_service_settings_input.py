"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#UpdateServiceSettingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.iam_role_arn


class UpdateServiceSettingsInput(TypedDict, closed=True):
    explorer_enabling_role_arn: NotRequired[
        "aws_sdk_ssm_quicksetup.types.iam_role_arn.IAMRoleArn"
    ]
    """<p>The IAM role used to enable Explorer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceSettingsInput) -> dict:
    out: dict = {}
    if "explorer_enabling_role_arn" in value:
        out["ExplorerEnablingRoleArn"] = value["explorer_enabling_role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateServiceSettingsInput:
    out: UpdateServiceSettingsInput = {}  # type: ignore[typeddict-item]
    if "ExplorerEnablingRoleArn" in data:
        out["explorer_enabling_role_arn"] = data["ExplorerEnablingRoleArn"]
    return out
