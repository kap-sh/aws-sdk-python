"""Generated from Smithy shape ``com.amazonaws.appconfig#AppliedExtension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.id
    import capo_appconfig.types.integer
    import capo_appconfig.types.parameter_value_map


class AppliedExtension(TypedDict, closed=True):
    extension_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The system-generated ID of the extension.</p>"""
    extension_association_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The system-generated ID for the association.</p>"""
    version_number: "capo_appconfig.types.integer.Integer"
    """<p>The extension version number.</p>"""
    parameters: NotRequired[
        "capo_appconfig.types.parameter_value_map.ParameterValueMap"
    ]
    """<p>One or more parameters for the actions called by the extension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppliedExtension) -> dict:
    out: dict = {}
    if "extension_id" in value:
        out["ExtensionId"] = value["extension_id"]
    if "extension_association_id" in value:
        out["ExtensionAssociationId"] = value["extension_association_id"]
    out["VersionNumber"] = value.get("version_number", 0)
    if "parameters" in value:
        import capo_appconfig.types.parameter_value_map

        out["Parameters"] = capo_appconfig.types.parameter_value_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> AppliedExtension:
    out: AppliedExtension = {}  # type: ignore[typeddict-item]
    if "ExtensionId" in data:
        out["extension_id"] = data["ExtensionId"]
    if "ExtensionAssociationId" in data:
        out["extension_association_id"] = data["ExtensionAssociationId"]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    else:
        out["version_number"] = 0
    if "Parameters" in data:
        import capo_appconfig.types.parameter_value_map

        out["parameters"] = capo_appconfig.types.parameter_value_map.deserialize_json(
            data["Parameters"]
        )
    return out
