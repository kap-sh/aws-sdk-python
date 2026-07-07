"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_input
    import aws_sdk_migration_hub_refactor_spaces.types.application_name
    import aws_sdk_migration_hub_refactor_spaces.types.client_token
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.proxy_type
    import aws_sdk_migration_hub_refactor_spaces.types.tag_map
    import aws_sdk_migration_hub_refactor_spaces.types.vpc_id


class CreateApplicationRequest(TypedDict, closed=True):
    name: "aws_sdk_migration_hub_refactor_spaces.types.application_name.ApplicationName"
    """<p>The name to use for the application. </p>"""
    environment_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The unique identifier of the environment.</p>"""
    vpc_id: "aws_sdk_migration_hub_refactor_spaces.types.vpc_id.VpcId"
    """<p>The ID of the virtual private cloud (VPC).</p>"""
    proxy_type: "aws_sdk_migration_hub_refactor_spaces.types.proxy_type.ProxyType"
    """<p>The proxy type of the proxy created within the application. </p>"""
    api_gateway_proxy: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_input.ApiGatewayProxyInput"
    ]
    """<p>A wrapper object holding the API Gateway endpoint type and stage name for the proxy. </p>"""
    tags: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags to assign to the application. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.</p>"""
    client_token: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["VpcId"] = value["vpc_id"]
    out["ProxyType"] = value["proxy_type"]
    if "api_gateway_proxy" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_input

        out["ApiGatewayProxy"] = (
            aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_input.serialize_json(
                value["api_gateway_proxy"]
            )
        )
    if "tags" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = (
            aws_sdk_migration_hub_refactor_spaces.types.tag_map.serialize_json(
                value["tags"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError("CreateApplicationRequest.vpc_id required")
    if "ProxyType" in data:
        out["proxy_type"] = data["ProxyType"]
    else:
        raise DeserializationError("CreateApplicationRequest.proxy_type required")
    if "ApiGatewayProxy" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_input

        out["api_gateway_proxy"] = (
            aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_input.deserialize_json(
                data["ApiGatewayProxy"]
            )
        )
    if "Tags" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = (
            aws_sdk_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
                data["Tags"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
