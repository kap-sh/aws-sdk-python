"""Generated from Smithy shape ``com.amazonaws.datazone#ConfigurableEnvironmentAction``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_datazone.types.configurable_action_parameter_list
    import aws_sdk_datazone.types.configurable_action_type_authorization

class ConfigurableEnvironmentAction(TypedDict):
    type: "str"
    """<p>The type of a configurable action in a Amazon DataZone environment.</p>"""
    auth: NotRequired["aws_sdk_datazone.types.configurable_action_type_authorization.ConfigurableActionTypeAuthorization"]
    """<p>The authentication type of a configurable action of a Amazon DataZone environment. </p>"""
    parameters: "aws_sdk_datazone.types.configurable_action_parameter_list.ConfigurableActionParameterList"
    """<p>The parameters of a configurable action in a Amazon DataZone environment.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableEnvironmentAction) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "auth" in value:
        import aws_sdk_datazone.types.configurable_action_type_authorization
        out["auth"] = aws_sdk_datazone.types.configurable_action_type_authorization.serialize_json(value["auth"])
    import aws_sdk_datazone.types.configurable_action_parameter_list
    out["parameters"] = aws_sdk_datazone.types.configurable_action_parameter_list.serialize_json(value["parameters"])
    return out


def deserialize_json(data: dict) -> ConfigurableEnvironmentAction:
    out: ConfigurableEnvironmentAction = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ConfigurableEnvironmentAction.type required")
    if "auth" in data:
        import aws_sdk_datazone.types.configurable_action_type_authorization
        out["auth"] = aws_sdk_datazone.types.configurable_action_type_authorization.deserialize_json(data["auth"])
    if "parameters" in data:
        import aws_sdk_datazone.types.configurable_action_parameter_list
        out["parameters"] = aws_sdk_datazone.types.configurable_action_parameter_list.deserialize_json(data["parameters"])
    else:
        raise DeserializationError("ConfigurableEnvironmentAction.parameters required")
    return out