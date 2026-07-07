"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.metadata
    import aws_sdk_chime_sdk_identity.types.user_name


class AppInstanceUserSummary(TypedDict, closed=True):
    app_instance_user_arn: NotRequired[
        "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    name: NotRequired["aws_sdk_chime_sdk_identity.types.user_name.UserName"]
    """<p>The name of an <code>AppInstanceUser</code>.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata of the <code>AppInstanceUser</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserSummary) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AppInstanceUserSummary:
    out: AppInstanceUserSummary = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserArn" in data:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    return out
