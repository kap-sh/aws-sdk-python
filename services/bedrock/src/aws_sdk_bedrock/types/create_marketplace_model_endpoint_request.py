"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.accept_eula
    import aws_sdk_bedrock.types.endpoint_config
    import aws_sdk_bedrock.types.endpoint_name
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.model_source_identifier
    import aws_sdk_bedrock.types.tag_list


class CreateMarketplaceModelEndpointRequest(TypedDict):
    model_source_identifier: (
        "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier"
    )
    """<p>The ARN of the model from Amazon Bedrock Marketplace that you want to deploy to the endpoint.</p>"""
    endpoint_config: "aws_sdk_bedrock.types.endpoint_config.EndpointConfig"
    """<p>The configuration for the endpoint, including the number and type of instances to use.</p>"""
    accept_eula: "aws_sdk_bedrock.types.accept_eula.AcceptEula"
    """<p>Indicates whether you accept the end-user license agreement (EULA) for the model. Set to <code>true</code> to accept the EULA.</p>"""
    endpoint_name: "aws_sdk_bedrock.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint. This name must be unique within your Amazon Web Services account and region.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>"""
    tags: NotRequired["aws_sdk_bedrock.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply to the underlying Amazon SageMaker endpoint. You can use these tags to organize and identify your Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    out["modelSourceIdentifier"] = value["model_source_identifier"]
    import aws_sdk_bedrock.types.endpoint_config

    out["endpointConfig"] = aws_sdk_bedrock.types.endpoint_config.serialize_json(
        value["endpoint_config"]
    )
    out["acceptEula"] = value.get("accept_eula", False)
    out["endpointName"] = value["endpoint_name"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMarketplaceModelEndpointRequest:
    out: CreateMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    if "modelSourceIdentifier" in data:
        out["model_source_identifier"] = data["modelSourceIdentifier"]
    else:
        raise DeserializationError(
            "CreateMarketplaceModelEndpointRequest.model_source_identifier required"
        )
    if "endpointConfig" in data:
        import aws_sdk_bedrock.types.endpoint_config

        out["endpoint_config"] = aws_sdk_bedrock.types.endpoint_config.deserialize_json(
            data["endpointConfig"]
        )
    else:
        raise DeserializationError(
            "CreateMarketplaceModelEndpointRequest.endpoint_config required"
        )
    if "acceptEula" in data:
        out["accept_eula"] = data["acceptEula"]
    else:
        out["accept_eula"] = False
    if "endpointName" in data:
        out["endpoint_name"] = data["endpointName"]
    else:
        raise DeserializationError(
            "CreateMarketplaceModelEndpointRequest.endpoint_name required"
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "tags" in data:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out
