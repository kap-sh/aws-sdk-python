"""Generated from Smithy shape ``com.amazonaws.appconfig#Environment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.environment_state
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.monitor_list
    import aws_sdk_appconfig.types.name


class Environment(TypedDict, closed=True):
    application_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The environment ID.</p>"""
    name: NotRequired["aws_sdk_appconfig.types.name.Name"]
    """<p>The name of the environment.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>The description of the environment.</p>"""
    state: NotRequired["aws_sdk_appconfig.types.environment_state.EnvironmentState"]
    """<p>The state of the environment. An environment can be in one of the following states: <code>READY_FOR_DEPLOYMENT</code>, <code>DEPLOYING</code>, <code>ROLLING_BACK</code>, or <code>ROLLED_BACK</code> </p>"""
    monitors: NotRequired["aws_sdk_appconfig.types.monitor_list.MonitorList"]
    """<p>Amazon CloudWatch alarms monitored during the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Environment) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import aws_sdk_appconfig.types.environment_state

        out["State"] = aws_sdk_appconfig.types.environment_state.serialize_json(
            value["state"]
        )
    if "monitors" in value:
        import aws_sdk_appconfig.types.monitor_list

        out["Monitors"] = aws_sdk_appconfig.types.monitor_list.serialize_json(
            value["monitors"]
        )
    return out


def deserialize_json(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import aws_sdk_appconfig.types.environment_state

        out["state"] = aws_sdk_appconfig.types.environment_state.deserialize_json(
            data["State"]
        )
    if "Monitors" in data:
        import aws_sdk_appconfig.types.monitor_list

        out["monitors"] = aws_sdk_appconfig.types.monitor_list.deserialize_json(
            data["Monitors"]
        )
    return out
