"""Generated from Smithy shape ``com.amazonaws.eks#AddonVersionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boolean
    import capo_eks.types.compatibilities
    import capo_eks.types.string
    import capo_eks.types.string_list


class AddonVersionInfo(TypedDict, closed=True):
    addon_version: NotRequired["capo_eks.types.string.String"]
    """<p>The version of the add-on.</p>"""
    architecture: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The architectures that the version supports.</p>"""
    compute_types: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>Indicates the compute type of the add-on version.</p>"""
    compatibilities: NotRequired["capo_eks.types.compatibilities.Compatibilities"]
    """<p>An object representing the compatibilities of a version.</p>"""
    requires_configuration: "capo_eks.types.boolean.Boolean"
    """<p>Whether the add-on requires configuration.</p>"""
    requires_iam_permissions: "capo_eks.types.boolean.Boolean"
    """<p>Indicates if the add-on requires IAM Permissions to operate, such as networking permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonVersionInfo) -> dict:
    out: dict = {}
    if "addon_version" in value:
        out["addonVersion"] = value["addon_version"]
    if "architecture" in value:
        import capo_eks.types.string_list

        out["architecture"] = capo_eks.types.string_list.serialize_json(
            value["architecture"]
        )
    if "compute_types" in value:
        import capo_eks.types.string_list

        out["computeTypes"] = capo_eks.types.string_list.serialize_json(
            value["compute_types"]
        )
    if "compatibilities" in value:
        import capo_eks.types.compatibilities

        out["compatibilities"] = capo_eks.types.compatibilities.serialize_json(
            value["compatibilities"]
        )
    out["requiresConfiguration"] = value.get("requires_configuration", False)
    out["requiresIamPermissions"] = value.get("requires_iam_permissions", False)
    return out


def deserialize_json(data: dict) -> AddonVersionInfo:
    out: AddonVersionInfo = {}  # type: ignore[typeddict-item]
    if "addonVersion" in data:
        out["addon_version"] = data["addonVersion"]
    if "architecture" in data:
        import capo_eks.types.string_list

        out["architecture"] = capo_eks.types.string_list.deserialize_json(
            data["architecture"]
        )
    if "computeTypes" in data:
        import capo_eks.types.string_list

        out["compute_types"] = capo_eks.types.string_list.deserialize_json(
            data["computeTypes"]
        )
    if "compatibilities" in data:
        import capo_eks.types.compatibilities

        out["compatibilities"] = capo_eks.types.compatibilities.deserialize_json(
            data["compatibilities"]
        )
    if "requiresConfiguration" in data:
        out["requires_configuration"] = data["requiresConfiguration"]
    else:
        out["requires_configuration"] = False
    if "requiresIamPermissions" in data:
        out["requires_iam_permissions"] = data["requiresIamPermissions"]
    else:
        out["requires_iam_permissions"] = False
    return out
