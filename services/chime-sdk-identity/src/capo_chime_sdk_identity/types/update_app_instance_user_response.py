"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#UpdateAppInstanceUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn


class UpdateAppInstanceUserResponse(TypedDict, closed=True):
    app_instance_user_arn: NotRequired[
        "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppInstanceUserResponse) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    return out


def deserialize_json(data: dict) -> UpdateAppInstanceUserResponse:
    out: UpdateAppInstanceUserResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserArn" in data:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    return out
