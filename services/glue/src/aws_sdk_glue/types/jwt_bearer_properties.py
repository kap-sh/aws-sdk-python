"""Generated from Smithy shape ``com.amazonaws.glue#JWTBearerProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.connector_property
    import aws_sdk_glue.types.connector_property_list
    import aws_sdk_glue.types.content_type
    import aws_sdk_glue.types.http_method


class JWTBearerProperties(TypedDict, closed=True):
    token_url: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The token endpoint URL where the JWT bearer token will be exchanged for an access token.</p>"""
    request_method: NotRequired["aws_sdk_glue.types.http_method.HTTPMethod"]
    """<p>The HTTP method to use when making JWT bearer token requests, typically POST.</p>"""
    content_type: NotRequired["aws_sdk_glue.types.content_type.ContentType"]
    """<p>The content type to use for JWT bearer token requests, such as application/x-www-form-urlencoded or application/json.</p>"""
    jwt_token: NotRequired["aws_sdk_glue.types.connector_property.ConnectorProperty"]
    """<p>The JWT token to be used in the bearer token grant flow for authentication.</p>"""
    token_url_parameters: NotRequired[
        "aws_sdk_glue.types.connector_property_list.ConnectorPropertyList"
    ]
    """<p>Additional parameters to include in token URL requests as key-value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JWTBearerProperties) -> dict:
    out: dict = {}
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
    if "jwt_token" in value:
        import aws_sdk_glue.types.connector_property

        out["JwtToken"] = aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(
            value["jwt_token"]
        )
    if "token_url_parameters" in value:
        import aws_sdk_glue.types.connector_property_list

        out["TokenUrlParameters"] = (
            aws_sdk_glue.types.connector_property_list.serialize_aws_json_1_1(
                value["token_url_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JWTBearerProperties:
    out: JWTBearerProperties = {}  # type: ignore[typeddict-item]
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
    if "JwtToken" in data:
        import aws_sdk_glue.types.connector_property

        out["jwt_token"] = (
            aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(
                data["JwtToken"]
            )
        )
    if "TokenUrlParameters" in data:
        import aws_sdk_glue.types.connector_property_list

        out["token_url_parameters"] = (
            aws_sdk_glue.types.connector_property_list.deserialize_aws_json_1_1(
                data["TokenUrlParameters"]
            )
        )
    return out
