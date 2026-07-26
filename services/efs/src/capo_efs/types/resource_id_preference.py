"""Generated from Smithy shape ``com.amazonaws.efs#ResourceIdPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.resource_id_type
    import capo_efs.types.resources


class ResourceIdPreference(TypedDict, closed=True):
    resource_id_type: NotRequired["capo_efs.types.resource_id_type.ResourceIdType"]
    """<p>Identifies the EFS resource ID preference, either <code>LONG_ID</code> (17 characters) or <code>SHORT_ID</code> (8 characters).</p>"""
    resources: NotRequired["capo_efs.types.resources.Resources"]
    """<p>Identifies the Amazon EFS resources to which the ID preference setting applies, <code>FILE_SYSTEM</code> and <code>MOUNT_TARGET</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdPreference) -> dict:
    out: dict = {}
    if "resource_id_type" in value:
        import capo_efs.types.resource_id_type

        out["ResourceIdType"] = capo_efs.types.resource_id_type.serialize_json(
            value["resource_id_type"]
        )
    if "resources" in value:
        import capo_efs.types.resources

        out["Resources"] = capo_efs.types.resources.serialize_json(value["resources"])
    return out


def deserialize_json(data: dict) -> ResourceIdPreference:
    out: ResourceIdPreference = {}  # type: ignore[typeddict-item]
    if "ResourceIdType" in data:
        import capo_efs.types.resource_id_type

        out["resource_id_type"] = capo_efs.types.resource_id_type.deserialize_json(
            data["ResourceIdType"]
        )
    if "Resources" in data:
        import capo_efs.types.resources

        out["resources"] = capo_efs.types.resources.deserialize_json(data["Resources"])
    return out
