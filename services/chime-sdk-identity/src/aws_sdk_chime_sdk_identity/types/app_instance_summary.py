"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.metadata
    import aws_sdk_chime_sdk_identity.types.non_empty_resource_name


class AppInstanceSummary(TypedDict):
    app_instance_arn: NotRequired["aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The <code>AppInstance</code> ARN.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the <code>AppInstance</code>.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata of the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceSummary) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AppInstanceSummary:
    out: AppInstanceSummary = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    return out
