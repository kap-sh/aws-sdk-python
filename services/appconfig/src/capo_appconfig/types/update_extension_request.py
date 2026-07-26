"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.actions_map
    import capo_appconfig.types.description
    import capo_appconfig.types.identifier
    import capo_appconfig.types.integer
    import capo_appconfig.types.parameter_map


class UpdateExtensionRequest(TypedDict, closed=True):
    extension_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>Information about the extension.</p>"""
    actions: NotRequired["capo_appconfig.types.actions_map.ActionsMap"]
    """<p>The actions defined in the extension.</p>"""
    parameters: NotRequired["capo_appconfig.types.parameter_map.ParameterMap"]
    """<p>One or more parameters for the actions called by the extension.</p>"""
    version_number: NotRequired["capo_appconfig.types.integer.Integer"]
    """<p>The extension version number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExtensionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "actions" in value:
        import capo_appconfig.types.actions_map

        out["Actions"] = capo_appconfig.types.actions_map.serialize_json(
            value["actions"]
        )
    if "parameters" in value:
        import capo_appconfig.types.parameter_map

        out["Parameters"] = capo_appconfig.types.parameter_map.serialize_json(
            value["parameters"]
        )
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> UpdateExtensionRequest:
    out: UpdateExtensionRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Actions" in data:
        import capo_appconfig.types.actions_map

        out["actions"] = capo_appconfig.types.actions_map.deserialize_json(
            data["Actions"]
        )
    if "Parameters" in data:
        import capo_appconfig.types.parameter_map

        out["parameters"] = capo_appconfig.types.parameter_map.deserialize_json(
            data["Parameters"]
        )
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    return out
