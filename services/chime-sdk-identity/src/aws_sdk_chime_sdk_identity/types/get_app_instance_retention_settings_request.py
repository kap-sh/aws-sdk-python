"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#GetAppInstanceRetentionSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn


class GetAppInstanceRetentionSettingsRequest(TypedDict, closed=True):
    app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppInstanceRetentionSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAppInstanceRetentionSettingsRequest:
    out: GetAppInstanceRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
