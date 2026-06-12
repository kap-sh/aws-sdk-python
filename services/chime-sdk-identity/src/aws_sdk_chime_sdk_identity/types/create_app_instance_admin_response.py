"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceAdminResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.identity


class CreateAppInstanceAdminResponse(TypedDict):
    app_instance_admin: NotRequired[
        "aws_sdk_chime_sdk_identity.types.identity.Identity"
    ]
    """<p>The ARN and name of the administrator, the ARN of the <code>AppInstance</code>, and the created and last-updated timestamps. All timestamps use epoch milliseconds.</p>"""
    app_instance_arn: NotRequired["aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the of the admin for the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceAdminResponse) -> dict:
    out: dict = {}
    if "app_instance_admin" in value:
        import aws_sdk_chime_sdk_identity.types.identity

        out["AppInstanceAdmin"] = (
            aws_sdk_chime_sdk_identity.types.identity.serialize_json(
                value["app_instance_admin"]
            )
        )
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    return out


def deserialize_json(data: dict) -> CreateAppInstanceAdminResponse:
    out: CreateAppInstanceAdminResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceAdmin" in data:
        import aws_sdk_chime_sdk_identity.types.identity

        out["app_instance_admin"] = (
            aws_sdk_chime_sdk_identity.types.identity.deserialize_json(
                data["AppInstanceAdmin"]
            )
        )
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    return out
