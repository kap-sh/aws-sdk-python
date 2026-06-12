"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorAuthenticationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.authentication_types
    import aws_sdk_glue.types.basic_authentication_properties
    import aws_sdk_glue.types.connector_o_auth2_properties
    import aws_sdk_glue.types.custom_authentication_properties


class ConnectorAuthenticationConfiguration(TypedDict):
    authentication_types: "aws_sdk_glue.types.authentication_types.AuthenticationTypes"
    """<p>A list of authentication types supported by this connection type, such as Basic, OAuth2, or Custom authentication methods.</p>"""
    o_auth2_properties: NotRequired[
        "aws_sdk_glue.types.connector_o_auth2_properties.ConnectorOAuth2Properties"
    ]
    basic_authentication_properties: NotRequired[
        "aws_sdk_glue.types.basic_authentication_properties.BasicAuthenticationProperties"
    ]
    custom_authentication_properties: NotRequired[
        "aws_sdk_glue.types.custom_authentication_properties.CustomAuthenticationProperties"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorAuthenticationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.authentication_types

    out["AuthenticationTypes"] = (
        aws_sdk_glue.types.authentication_types.serialize_aws_json_1_1(
            value["authentication_types"]
        )
    )
    if "o_auth2_properties" in value:
        import aws_sdk_glue.types.connector_o_auth2_properties

        out["OAuth2Properties"] = (
            aws_sdk_glue.types.connector_o_auth2_properties.serialize_aws_json_1_1(
                value["o_auth2_properties"]
            )
        )
    if "basic_authentication_properties" in value:
        import aws_sdk_glue.types.basic_authentication_properties

        out["BasicAuthenticationProperties"] = (
            aws_sdk_glue.types.basic_authentication_properties.serialize_aws_json_1_1(
                value["basic_authentication_properties"]
            )
        )
    if "custom_authentication_properties" in value:
        import aws_sdk_glue.types.custom_authentication_properties

        out["CustomAuthenticationProperties"] = (
            aws_sdk_glue.types.custom_authentication_properties.serialize_aws_json_1_1(
                value["custom_authentication_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorAuthenticationConfiguration:
    out: ConnectorAuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "AuthenticationTypes" in data:
        import aws_sdk_glue.types.authentication_types

        out["authentication_types"] = (
            aws_sdk_glue.types.authentication_types.deserialize_aws_json_1_1(
                data["AuthenticationTypes"]
            )
        )
    else:
        raise DeserializationError(
            "ConnectorAuthenticationConfiguration.authentication_types required"
        )
    if "OAuth2Properties" in data:
        import aws_sdk_glue.types.connector_o_auth2_properties

        out["o_auth2_properties"] = (
            aws_sdk_glue.types.connector_o_auth2_properties.deserialize_aws_json_1_1(
                data["OAuth2Properties"]
            )
        )
    if "BasicAuthenticationProperties" in data:
        import aws_sdk_glue.types.basic_authentication_properties

        out["basic_authentication_properties"] = (
            aws_sdk_glue.types.basic_authentication_properties.deserialize_aws_json_1_1(
                data["BasicAuthenticationProperties"]
            )
        )
    if "CustomAuthenticationProperties" in data:
        import aws_sdk_glue.types.custom_authentication_properties

        out["custom_authentication_properties"] = (
            aws_sdk_glue.types.custom_authentication_properties.deserialize_aws_json_1_1(
                data["CustomAuthenticationProperties"]
            )
        )
    return out
