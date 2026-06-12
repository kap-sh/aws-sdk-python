"""Generated from Smithy shape ``com.amazonaws.glue#AuthConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.properties_map
    import aws_sdk_glue.types.property


class AuthConfiguration(TypedDict):
    authentication_type: "aws_sdk_glue.types.property.Property"
    """<p>The type of authentication for a connection.</p>"""
    secret_arn: NotRequired["aws_sdk_glue.types.property.Property"]
    """<p>The Amazon Resource Name (ARN) for the Secrets Manager.</p>"""
    o_auth2_properties: NotRequired["aws_sdk_glue.types.properties_map.PropertiesMap"]
    """<p>A map of key-value pairs for the OAuth2 properties. Each value is a a <code>Property</code> object.</p>"""
    basic_authentication_properties: NotRequired[
        "aws_sdk_glue.types.properties_map.PropertiesMap"
    ]
    """<p>A map of key-value pairs for the OAuth2 properties. Each value is a a <code>Property</code> object.</p>"""
    custom_authentication_properties: NotRequired[
        "aws_sdk_glue.types.properties_map.PropertiesMap"
    ]
    """<p>A map of key-value pairs for the custom authentication properties. Each value is a a <code>Property</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.property

    out["AuthenticationType"] = aws_sdk_glue.types.property.serialize_aws_json_1_1(
        value["authentication_type"]
    )
    if "secret_arn" in value:
        import aws_sdk_glue.types.property

        out["SecretArn"] = aws_sdk_glue.types.property.serialize_aws_json_1_1(
            value["secret_arn"]
        )
    if "o_auth2_properties" in value:
        import aws_sdk_glue.types.properties_map

        out["OAuth2Properties"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["o_auth2_properties"]
            )
        )
    if "basic_authentication_properties" in value:
        import aws_sdk_glue.types.properties_map

        out["BasicAuthenticationProperties"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["basic_authentication_properties"]
            )
        )
    if "custom_authentication_properties" in value:
        import aws_sdk_glue.types.properties_map

        out["CustomAuthenticationProperties"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["custom_authentication_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthConfiguration:
    out: AuthConfiguration = {}  # type: ignore[typeddict-item]
    if "AuthenticationType" in data:
        import aws_sdk_glue.types.property

        out["authentication_type"] = (
            aws_sdk_glue.types.property.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    else:
        raise DeserializationError("AuthConfiguration.authentication_type required")
    if "SecretArn" in data:
        import aws_sdk_glue.types.property

        out["secret_arn"] = aws_sdk_glue.types.property.deserialize_aws_json_1_1(
            data["SecretArn"]
        )
    if "OAuth2Properties" in data:
        import aws_sdk_glue.types.properties_map

        out["o_auth2_properties"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["OAuth2Properties"]
            )
        )
    if "BasicAuthenticationProperties" in data:
        import aws_sdk_glue.types.properties_map

        out["basic_authentication_properties"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["BasicAuthenticationProperties"]
            )
        )
    if "CustomAuthenticationProperties" in data:
        import aws_sdk_glue.types.properties_map

        out["custom_authentication_properties"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["CustomAuthenticationProperties"]
            )
        )
    return out
