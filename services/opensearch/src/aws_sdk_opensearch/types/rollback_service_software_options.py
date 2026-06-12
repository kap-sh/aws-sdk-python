"""Generated from Smithy shape ``com.amazonaws.opensearch#RollbackServiceSoftwareOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.string


class RollbackServiceSoftwareOptions(TypedDict):
    current_version: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The current service software version on the domain.</p>"""
    new_version: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The service software version that the domain will roll back to.</p>"""
    rollback_available: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether a service software rollback is available for the domain.</p>"""
    description: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>A description of the rollback status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackServiceSoftwareOptions) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["CurrentVersion"] = value["current_version"]
    if "new_version" in value:
        out["NewVersion"] = value["new_version"]
    if "rollback_available" in value:
        out["RollbackAvailable"] = value["rollback_available"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> RollbackServiceSoftwareOptions:
    out: RollbackServiceSoftwareOptions = {}  # type: ignore[typeddict-item]
    if "CurrentVersion" in data:
        out["current_version"] = data["CurrentVersion"]
    if "NewVersion" in data:
        out["new_version"] = data["NewVersion"]
    if "RollbackAvailable" in data:
        out["rollback_available"] = data["RollbackAvailable"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
