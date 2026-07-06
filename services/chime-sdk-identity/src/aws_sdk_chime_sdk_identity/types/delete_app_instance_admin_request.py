"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DeleteAppInstanceAdminRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn


class DeleteAppInstanceAdminRequest(TypedDict, closed=True):
    app_instance_admin_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>'s administrator.</p>"""
    app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppInstanceAdminRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppInstanceAdminRequest:
    out: DeleteAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
    return out
