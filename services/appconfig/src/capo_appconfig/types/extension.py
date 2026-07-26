"""Generated from Smithy shape ``com.amazonaws.appconfig#Extension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.actions_map
    import capo_appconfig.types.arn
    import capo_appconfig.types.description
    import capo_appconfig.types.id
    import capo_appconfig.types.integer
    import capo_appconfig.types.name
    import capo_appconfig.types.parameter_map


class Extension(TypedDict, closed=True):
    id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The system-generated ID of the extension.</p>"""
    name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The extension name.</p>"""
    version_number: "capo_appconfig.types.integer.Integer"
    """<p>The extension version number.</p>"""
    arn: NotRequired["capo_appconfig.types.arn.Arn"]
    """<p>The system-generated Amazon Resource Name (ARN) for the extension.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>Information about the extension.</p>"""
    actions: NotRequired["capo_appconfig.types.actions_map.ActionsMap"]
    """<p>The actions defined in the extension.</p>"""
    parameters: NotRequired["capo_appconfig.types.parameter_map.ParameterMap"]
    """<p>The parameters accepted by the extension. You specify parameter values when you associate the extension to an AppConfig resource by using the <code>CreateExtensionAssociation</code> API action. For Lambda extension actions, these parameters are included in the Lambda request object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Extension) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    out["VersionNumber"] = value.get("version_number", 0)
    if "arn" in value:
        out["Arn"] = value["arn"]
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
    return out


def deserialize_json(data: dict) -> Extension:
    out: Extension = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    else:
        out["version_number"] = 0
    if "Arn" in data:
        out["arn"] = data["Arn"]
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
    return out
