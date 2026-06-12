"""Generated from Smithy shape ``com.amazonaws.iot#UpdateAuthorizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.authorizer_function_arn
    import aws_sdk_iot.types.authorizer_name
    import aws_sdk_iot.types.authorizer_status
    import aws_sdk_iot.types.enable_caching_for_http
    import aws_sdk_iot.types.public_key_map
    import aws_sdk_iot.types.token_key_name


class UpdateAuthorizerRequest(TypedDict):
    authorizer_name: "aws_sdk_iot.types.authorizer_name.AuthorizerName"
    """<p>The authorizer name.</p>"""
    authorizer_function_arn: NotRequired[
        "aws_sdk_iot.types.authorizer_function_arn.AuthorizerFunctionArn"
    ]
    """<p>The ARN of the authorizer's Lambda function.</p>"""
    token_key_name: NotRequired["aws_sdk_iot.types.token_key_name.TokenKeyName"]
    """<p>The key used to extract the token from the HTTP headers. </p>"""
    token_signing_public_keys: NotRequired[
        "aws_sdk_iot.types.public_key_map.PublicKeyMap"
    ]
    """<p>The public keys used to verify the token signature.</p>"""
    status: NotRequired["aws_sdk_iot.types.authorizer_status.AuthorizerStatus"]
    """<p>The status of the update authorizer request.</p>"""
    enable_caching_for_http: NotRequired[
        "aws_sdk_iot.types.enable_caching_for_http.EnableCachingForHttp"
    ]
    """<p>When <code>true</code>, the result from the authorizer’s Lambda function is cached for the time specified in <code>refreshAfterInSeconds</code>. The cached result is used while the device reuses the same HTTP connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAuthorizerRequest) -> dict:
    out: dict = {}
    if "authorizer_function_arn" in value:
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
    if "enable_caching_for_http" in value:
        out["enableCachingForHttp"] = value["enable_caching_for_http"]
    return out


def deserialize_json(data: dict) -> UpdateAuthorizerRequest:
    out: UpdateAuthorizerRequest = {}  # type: ignore[typeddict-item]
    if "authorizerFunctionArn" in data:
        out["authorizer_function_arn"] = data["authorizerFunctionArn"]
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
    if "enableCachingForHttp" in data:
        out["enable_caching_for_http"] = data["enableCachingForHttp"]
    return out
