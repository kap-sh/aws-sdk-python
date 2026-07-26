"""Generated from Smithy shape ``com.amazonaws.iot#UpdateAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.authorizer_function_arn
    import capo_iot.types.authorizer_name
    import capo_iot.types.authorizer_status
    import capo_iot.types.enable_caching_for_http
    import capo_iot.types.public_key_map
    import capo_iot.types.token_key_name


class UpdateAuthorizerRequest(TypedDict, closed=True):
    authorizer_name: "capo_iot.types.authorizer_name.AuthorizerName"
    """<p>The authorizer name.</p>"""
    authorizer_function_arn: NotRequired[
        "capo_iot.types.authorizer_function_arn.AuthorizerFunctionArn"
    ]
    """<p>The ARN of the authorizer's Lambda function.</p>"""
    token_key_name: NotRequired["capo_iot.types.token_key_name.TokenKeyName"]
    """<p>The key used to extract the token from the HTTP headers. </p>"""
    token_signing_public_keys: NotRequired["capo_iot.types.public_key_map.PublicKeyMap"]
    """<p>The public keys used to verify the token signature.</p>"""
    status: NotRequired["capo_iot.types.authorizer_status.AuthorizerStatus"]
    """<p>The status of the update authorizer request.</p>"""
    enable_caching_for_http: NotRequired[
        "capo_iot.types.enable_caching_for_http.EnableCachingForHttp"
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
        import capo_iot.types.public_key_map

        out["tokenSigningPublicKeys"] = capo_iot.types.public_key_map.serialize_json(
            value["token_signing_public_keys"]
        )
    if "status" in value:
        import capo_iot.types.authorizer_status

        out["status"] = capo_iot.types.authorizer_status.serialize_json(value["status"])
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
        import capo_iot.types.public_key_map

        out["token_signing_public_keys"] = (
            capo_iot.types.public_key_map.deserialize_json(
                data["tokenSigningPublicKeys"]
            )
        )
    if "status" in data:
        import capo_iot.types.authorizer_status

        out["status"] = capo_iot.types.authorizer_status.deserialize_json(
            data["status"]
        )
    if "enableCachingForHttp" in data:
        out["enable_caching_for_http"] = data["enableCachingForHttp"]
    return out
