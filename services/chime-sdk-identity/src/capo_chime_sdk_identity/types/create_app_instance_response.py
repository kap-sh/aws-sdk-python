"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn


class CreateAppInstanceResponse(TypedDict, closed=True):
    app_instance_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The Amazon Resource Number (ARN) of the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceResponse) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    return out


def deserialize_json(data: dict) -> CreateAppInstanceResponse:
    out: CreateAppInstanceResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    return out
