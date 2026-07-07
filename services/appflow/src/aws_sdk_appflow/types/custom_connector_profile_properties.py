"""Generated from Smithy shape ``com.amazonaws.appflow#CustomConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.o_auth2_properties
    import aws_sdk_appflow.types.profile_properties_map


class CustomConnectorProfileProperties(TypedDict, closed=True):
    profile_properties: NotRequired[
        "aws_sdk_appflow.types.profile_properties_map.ProfilePropertiesMap"
    ]
    """<p>A map of properties that are required to create a profile for the custom connector.</p>"""
    o_auth2_properties: NotRequired[
        "aws_sdk_appflow.types.o_auth2_properties.OAuth2Properties"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CustomConnectorProfileProperties) -> dict:
    out: dict = {}
    if "profile_properties" in value:
        import aws_sdk_appflow.types.profile_properties_map

        out["profileProperties"] = (
            aws_sdk_appflow.types.profile_properties_map.serialize_json(
                value["profile_properties"]
            )
        )
    if "o_auth2_properties" in value:
        import aws_sdk_appflow.types.o_auth2_properties

        out["oAuth2Properties"] = (
            aws_sdk_appflow.types.o_auth2_properties.serialize_json(
                value["o_auth2_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomConnectorProfileProperties:
    out: CustomConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if "profileProperties" in data:
        import aws_sdk_appflow.types.profile_properties_map

        out["profile_properties"] = (
            aws_sdk_appflow.types.profile_properties_map.deserialize_json(
                data["profileProperties"]
            )
        )
    if "oAuth2Properties" in data:
        import aws_sdk_appflow.types.o_auth2_properties

        out["o_auth2_properties"] = (
            aws_sdk_appflow.types.o_auth2_properties.deserialize_json(
                data["oAuth2Properties"]
            )
        )
    return out
