"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.id
    import capo_appconfig.types.monitor_list
    import capo_appconfig.types.name


class UpdateEnvironmentRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    environment_id: "capo_appconfig.types.id.Id"
    """<p>The environment ID.</p>"""
    name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The name of the environment.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the environment.</p>"""
    monitors: NotRequired["capo_appconfig.types.monitor_list.MonitorList"]
    """<p>Amazon CloudWatch alarms to monitor during the deployment process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "monitors" in value:
        import capo_appconfig.types.monitor_list

        out["Monitors"] = capo_appconfig.types.monitor_list.serialize_json(
            value["monitors"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentRequest:
    out: UpdateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Monitors" in data:
        import capo_appconfig.types.monitor_list

        out["monitors"] = capo_appconfig.types.monitor_list.deserialize_json(
            data["Monitors"]
        )
    return out
