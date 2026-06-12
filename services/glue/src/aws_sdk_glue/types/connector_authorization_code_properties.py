"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorAuthorizationCodeProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.connector_property
    import aws_sdk_glue.types.connector_property_list
    import aws_sdk_glue.types.content_type
    import aws_sdk_glue.types.http_method


class ConnectorAuthorizationCodeProperties(TypedDict):
    authorization_code_url: NotRequired[
        "aws_sdk_glue.types.connector_property.ConnectorProperty"
    ]
    """<p>The authorization endpoint URL where users will be redirected to grant authorization.</p>"""
    authorization_code: NotRequired[
        "aws_sdk_glue.types.connector_property.ConnectorProperty"
    ]
    """<p>The authorization code received from the authorization server after user consent.</p>"""
    redirect_uri: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The redirect URI that must match the URI registered with the authorization server.</p>"""
    token_url: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The token endpoint URL where the authorization code will be exchanged for an access token.</p>"""
    request_method: NotRequired["aws_sdk_glue.types.http_method.HTTPMethod"]
    """<p>The HTTP method to use when making token exchange requests, typically POST.</p>"""
    content_type: NotRequired["aws_sdk_glue.types.content_type.ContentType"]
    """<p>The content type to use for token exchange requests, such as application/x-www-form-urlencoded or application/json.</p>"""
    client_id: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The OAuth2 client identifier provided by the authorization server.</p>"""
    client_secret: NotRequired[
        "aws_sdk_glue.types.connector_property.ConnectorProperty"
    ]
    """<p>The OAuth2 client secret provided by the authorization server.</p>"""
    scope: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The OAuth2 scope that defines the level of access requested for the authorization code flow.</p>"""
    prompt: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The OAuth2 prompt parameter that controls the authorization server's behavior during user authentication.</p>"""
    token_url_parameters: NotRequired[
        "aws_sdk_glue.types.connector_property_list.ConnectorPropertyList"
    ]
    """<p>Additional parameters to include in token URL requests as key-value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorAuthorizationCodeProperties) -> dict:
    out: dict = {}
    if "authorization_code_url" in value:
        import aws_sdk_glue.types.connector_property

        out["AuthorizationCodeUrl"] = (
            aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
                value["authorization_code_url"]
            )
        )
    if "authorization_code" in value:
        import aws_sdk_glue.types.connector_property

        out["AuthorizationCode"] = (
            aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
                value["authorization_code"]
            )
        )
    if "redirect_uri" in value:
        import aws_sdk_glue.types.connector_property

        out["RedirectUri"] = (
            aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
                value["redirect_uri"]
            )
        )
    if "token_url" in value:
        import aws_sdk_glue.types.connector_property

        out["TokenUrl"] = aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
            value["token_url"]
        )
    if "request_method" in value:
        import aws_sdk_glue.types.http_method

        out["RequestMethod"] = aws_sdk_glue.types.http_method.serialize_aws_json_1_1(
            value["request_method"]
        )
    if "content_type" in value:
        import aws_sdk_glue.types.content_type

        out["ContentType"] = aws_sdk_glue.types.content_type.serialize_aws_json_1_1(
            value["content_type"]
        )
    if "client_id" in value:
        import aws_sdk_glue.types.connector_property

        out["ClientId"] = aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
            value["client_id"]
        )
    if "client_secret" in value:
        import aws_sdk_glue.types.connector_property

        out["ClientSecret"] = (
            aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
                value["client_secret"]
            )
        )
    if "scope" in value:
        import aws_sdk_glue.types.connector_property

        out["Scope"] = aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
            value["scope"]
        )
    if "prompt" in value:
        import aws_sdk_glue.types.connector_property

        out["Prompt"] = aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
            value["prompt"]
        )
    if "token_url_parameters" in value:
        import aws_sdk_glue.types.connector_property_list

        out["TokenUrlParameters"] = (
            aws_sdk_glue.types.connector_property_list.serialize_aws_json_1_1(
                value["token_url_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorAuthorizationCodeProperties:
    out: ConnectorAuthorizationCodeProperties = {}  # type: ignore[typeddict-item]
    if "AuthorizationCodeUrl" in data:
        import aws_sdk_glue.types.connector_property

        out["authorization_code_url"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["AuthorizationCodeUrl"]
            )
        )
    if "AuthorizationCode" in data:
        import aws_sdk_glue.types.connector_property

        out["authorization_code"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["AuthorizationCode"]
            )
        )
    if "RedirectUri" in data:
        import aws_sdk_glue.types.connector_property

        out["redirect_uri"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["RedirectUri"]
            )
        )
    if "TokenUrl" in data:
        import aws_sdk_glue.types.connector_property

        out["token_url"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["TokenUrl"]
            )
        )
    if "RequestMethod" in data:
        import aws_sdk_glue.types.http_method

        out["request_method"] = aws_sdk_glue.types.http_method.deserialize_aws_json_1_1(
            data["RequestMethod"]
        )
    if "ContentType" in data:
        import aws_sdk_glue.types.content_type

        out["content_type"] = aws_sdk_glue.types.content_type.deserialize_aws_json_1_1(
            data["ContentType"]
        )
    if "ClientId" in data:
        import aws_sdk_glue.types.connector_property

        out["client_id"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["ClientId"]
            )
        )
    if "ClientSecret" in data:
        import aws_sdk_glue.types.connector_property

        out["client_secret"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["ClientSecret"]
            )
        )
    if "Scope" in data:
        import aws_sdk_glue.types.connector_property

        out["scope"] = aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
            data["Scope"]
        )
    if "Prompt" in data:
        import aws_sdk_glue.types.connector_property

        out["prompt"] = aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
            data["Prompt"]
        )
    if "TokenUrlParameters" in data:
        import aws_sdk_glue.types.connector_property_list

        out["token_url_parameters"] = (
            aws_sdk_glue.types.connector_property_list.deserialize_aws_json_1_1(
                data["TokenUrlParameters"]
            )
        )
    return out
