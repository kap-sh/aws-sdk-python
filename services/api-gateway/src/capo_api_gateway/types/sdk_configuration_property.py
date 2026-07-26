"""Generated from Smithy shape ``com.amazonaws.apigateway#SdkConfigurationProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.string


class SdkConfigurationProperty(TypedDict, closed=True):
    name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of a an SdkType configuration property.</p>"""
    friendly_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The user-friendly name of an SdkType configuration property.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of an SdkType configuration property.</p>"""
    required: "capo_api_gateway.types.boolean.Boolean"
    """<p>A boolean flag of an SdkType configuration property to indicate if the associated SDK configuration property is required (<code>true</code>) or not (<code>false</code>).</p>"""
    default_value: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The default value of an SdkType configuration property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SdkConfigurationProperty) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "friendly_name" in value:
        out["friendlyName"] = value["friendly_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["required"] = value.get("required", False)
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> SdkConfigurationProperty:
    out: SdkConfigurationProperty = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "friendlyName" in data:
        out["friendly_name"] = data["friendlyName"]
    if "description" in data:
        out["description"] = data["description"]
    if "required" in data:
        out["required"] = data["required"]
    else:
        out["required"] = False
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    return out
