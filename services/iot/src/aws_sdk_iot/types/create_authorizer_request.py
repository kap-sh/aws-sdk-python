"""Generated from Smithy shape ``com.amazonaws.iot#CreateAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.authorizer_function_arn
    import aws_sdk_iot.types.authorizer_name
    import aws_sdk_iot.types.authorizer_status
    import aws_sdk_iot.types.boolean_key
    import aws_sdk_iot.types.enable_caching_for_http
    import aws_sdk_iot.types.public_key_map
    import aws_sdk_iot.types.tag_list
    import aws_sdk_iot.types.token_key_name


class CreateAuthorizerRequest(TypedDict, closed=True):
    authorizer_name: "aws_sdk_iot.types.authorizer_name.AuthorizerName"
    """<p>The authorizer name.</p>"""
    authorizer_function_arn: (
        "aws_sdk_iot.types.authorizer_function_arn.AuthorizerFunctionArn"
    )
    """<p>The ARN of the authorizer's Lambda function.</p>"""
    token_key_name: NotRequired["aws_sdk_iot.types.token_key_name.TokenKeyName"]
    """<p>The name of the token key used to extract the token from the HTTP headers.</p>"""
    token_signing_public_keys: NotRequired[
        "aws_sdk_iot.types.public_key_map.PublicKeyMap"
    ]
    """<p>The public keys used to verify the digital signature returned by your custom authentication service.</p>"""
    status: NotRequired["aws_sdk_iot.types.authorizer_status.AuthorizerStatus"]
    """<p>The status of the create authorizer request.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    r"""<p>Metadata which can be used to manage the custom authorizer.</p> <note> <p>For URI Request parameters use format: ...key1=value1&key2=value2...</p> <p>For the CLI command-line parameter use format: &&tags \"key1=value1&key2=value2...\"</p> <p>For the cli-input-json file use format: \"tags\": \"key1=value1&key2=value2...\"</p> </note>"""
    signing_disabled: NotRequired["aws_sdk_iot.types.boolean_key.BooleanKey"]
    """<p>Specifies whether IoT validates the token signature in an authorization request.</p>"""
    enable_caching_for_http: NotRequired[
        "aws_sdk_iot.types.enable_caching_for_http.EnableCachingForHttp"
    ]
    """<p>When <code>true</code>, the result from the authorizer’s Lambda function is cached for clients that use persistent HTTP connections. The results are cached for the time specified by the Lambda function in <code>refreshAfterInSeconds</code>. This value does not affect authorization of clients that use MQTT connections.</p> <p>The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAuthorizerRequest) -> dict:
    out: dict = {}
    out["authorizerFunctionArn"] = value["authorizer_function_arn"]
    if "token_key_name" in value:
        out["tokenKeyName"] = value["token_key_name"]
    if "token_signing_public_keys" in value:
        import aws_sdk_iot.types.public_key_map

        out["tokenSigningPublicKeys"] = aws_sdk_iot.types.public_key_map.serialize_json(
            value["token_signing_public_keys"]
        )
    if "status" in value:
        import aws_sdk_iot.types.authorizer_status

        out["status"] = aws_sdk_iot.types.authorizer_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    if "signing_disabled" in value:
        out["signingDisabled"] = value["signing_disabled"]
    if "enable_caching_for_http" in value:
        out["enableCachingForHttp"] = value["enable_caching_for_http"]
    return out


def deserialize_json(data: dict) -> CreateAuthorizerRequest:
    out: CreateAuthorizerRequest = {}  # type: ignore[typeddict-item]
    if "authorizerFunctionArn" in data:
        out["authorizer_function_arn"] = data["authorizerFunctionArn"]
    else:
        raise DeserializationError(
            "CreateAuthorizerRequest.authorizer_function_arn required"
        )
    if "tokenKeyName" in data:
        out["token_key_name"] = data["tokenKeyName"]
    if "tokenSigningPublicKeys" in data:
        import aws_sdk_iot.types.public_key_map

        out["token_signing_public_keys"] = (
            aws_sdk_iot.types.public_key_map.deserialize_json(
                data["tokenSigningPublicKeys"]
            )
        )
    if "status" in data:
        import aws_sdk_iot.types.authorizer_status

        out["status"] = aws_sdk_iot.types.authorizer_status.deserialize_json(
            data["status"]
        )
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    if "signingDisabled" in data:
        out["signing_disabled"] = data["signingDisabled"]
    if "enableCachingForHttp" in data:
        out["enable_caching_for_http"] = data["enableCachingForHttp"]
    return out
