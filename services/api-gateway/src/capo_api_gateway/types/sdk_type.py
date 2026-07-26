"""Generated from Smithy shape ``com.amazonaws.apigateway#SdkType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_sdk_configuration_property
    import capo_api_gateway.types.string


class SdkType(TypedDict, closed=True):
    id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier of an SdkType instance.</p>"""
    friendly_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The user-friendly name of an SdkType instance.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of an SdkType.</p>"""
    configuration_properties: NotRequired[
        "capo_api_gateway.types.list_of_sdk_configuration_property.ListOfSdkConfigurationProperty"
    ]
    """<p>A list of configuration properties of an SdkType.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SdkType) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "friendly_name" in value:
        out["friendlyName"] = value["friendly_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "configuration_properties" in value:
        import capo_api_gateway.types.list_of_sdk_configuration_property

        out["configurationProperties"] = (
            capo_api_gateway.types.list_of_sdk_configuration_property.serialize_json(
                value["configuration_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> SdkType:
    out: SdkType = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "friendlyName" in data:
        out["friendly_name"] = data["friendlyName"]
    if "description" in data:
        out["description"] = data["description"]
    if "configurationProperties" in data:
        import capo_api_gateway.types.list_of_sdk_configuration_property

        out["configuration_properties"] = (
            capo_api_gateway.types.list_of_sdk_configuration_property.deserialize_json(
                data["configurationProperties"]
            )
        )
    return out
