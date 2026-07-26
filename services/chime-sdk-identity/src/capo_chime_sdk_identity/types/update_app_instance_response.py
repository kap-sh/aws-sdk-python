"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#UpdateAppInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn


class UpdateAppInstanceResponse(TypedDict, closed=True):
    app_instance_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppInstanceResponse) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    return out


def deserialize_json(data: dict) -> UpdateAppInstanceResponse:
    out: UpdateAppInstanceResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    return out
