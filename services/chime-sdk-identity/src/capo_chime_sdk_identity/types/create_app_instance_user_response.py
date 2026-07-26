"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn


class CreateAppInstanceUserResponse(TypedDict, closed=True):
    app_instance_user_arn: NotRequired[
        "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The user's ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceUserResponse) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    return out


def deserialize_json(data: dict) -> CreateAppInstanceUserResponse:
    out: CreateAppInstanceUserResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserArn" in data:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    return out
