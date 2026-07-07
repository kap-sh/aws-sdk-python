"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.arn
    import aws_sdk_bedrock.types.endpoint_config
    import aws_sdk_bedrock.types.idempotency_token


class UpdateMarketplaceModelEndpointRequest(TypedDict, closed=True):
    endpoint_arn: "aws_sdk_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint you want to update.</p>"""
    endpoint_config: "aws_sdk_bedrock.types.endpoint_config.EndpointConfig"
    """<p>The new configuration for the endpoint, including the number and type of instances to use.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.endpoint_config

    out["endpointConfig"] = aws_sdk_bedrock.types.endpoint_config.serialize_json(
        value["endpoint_config"]
    )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpdateMarketplaceModelEndpointRequest:
    out: UpdateMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    if "endpointConfig" in data:
        import aws_sdk_bedrock.types.endpoint_config

        out["endpoint_config"] = aws_sdk_bedrock.types.endpoint_config.deserialize_json(
            data["endpointConfig"]
        )
    else:
        raise DeserializationError(
            "UpdateMarketplaceModelEndpointRequest.endpoint_config required"
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
