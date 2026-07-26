"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.non_empty_resource_name


class AppInstanceSummary(TypedDict, closed=True):
    app_instance_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The <code>AppInstance</code> ARN.</p>"""
    name: NotRequired[
        "capo_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the <code>AppInstance</code>.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
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
