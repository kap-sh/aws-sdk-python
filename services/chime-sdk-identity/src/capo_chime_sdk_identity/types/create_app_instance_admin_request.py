"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceAdminRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn


class CreateAppInstanceAdminRequest(TypedDict, closed=True):
    app_instance_admin_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the administrator of the current <code>AppInstance</code>.</p>"""
    app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceAdminRequest) -> dict:
    out: dict = {}
    out["AppInstanceAdminArn"] = value["app_instance_admin_arn"]
    return out


def deserialize_json(data: dict) -> CreateAppInstanceAdminRequest:
    out: CreateAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
    if "AppInstanceAdminArn" in data:
        out["app_instance_admin_arn"] = data["AppInstanceAdminArn"]
    else:
        raise DeserializationError(
            "CreateAppInstanceAdminRequest.app_instance_admin_arn required"
        )
    return out
