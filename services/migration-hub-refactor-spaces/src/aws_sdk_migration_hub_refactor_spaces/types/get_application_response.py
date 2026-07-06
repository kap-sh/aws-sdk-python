"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.account_id
    import aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_config
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.application_name
    import aws_sdk_migration_hub_refactor_spaces.types.application_state
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.error_response
    import aws_sdk_migration_hub_refactor_spaces.types.proxy_type
    import aws_sdk_migration_hub_refactor_spaces.types.resource_arn
    import aws_sdk_migration_hub_refactor_spaces.types.tag_map
    import aws_sdk_migration_hub_refactor_spaces.types.timestamp
    import aws_sdk_migration_hub_refactor_spaces.types.vpc_id


class GetApplicationResponse(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_name.ApplicationName"
    ]
    """<p>The name of the application.</p>"""
    arn: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    owner_account_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the application owner (which is always the same as the environment owner account ID).</p>"""
    created_by_account_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the application creator. </p>"""
    application_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The unique identifier of the application.</p>"""
    environment_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The unique identifier of the environment.</p>"""
    vpc_id: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.vpc_id.VpcId"]
    """<p>The ID of the virtual private cloud (VPC). </p>"""
    proxy_type: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.proxy_type.ProxyType"
    ]
    """<p>The proxy type of the proxy created within the application. </p>"""
    api_gateway_proxy: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_config.ApiGatewayProxyConfig"
    ]
    """<p>The endpoint URL of the API Gateway proxy. </p>"""
    state: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_state.ApplicationState"
    ]
    """<p>The current state of the application. </p>"""
    tags: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags assigned to the application. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair. </p>"""
    error: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.error_response.ErrorResponse"
    ]
    """<p>Any error associated with the application resource. </p>"""
    last_updated_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the application was last updated. </p>"""
    created_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the application is created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "created_by_account_id" in value:
        out["CreatedByAccountId"] = value["created_by_account_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "proxy_type" in value:
        out["ProxyType"] = value["proxy_type"]
    if "api_gateway_proxy" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_config

        out["ApiGatewayProxy"] = (
            aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_config.serialize_json(
                value["api_gateway_proxy"]
            )
        )
    if "state" in value:
        out["State"] = value["state"]
    if "tags" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = (
            aws_sdk_migration_hub_refactor_spaces.types.tag_map.serialize_json(
                value["tags"]
            )
        )
    if "error" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.error_response

        out["Error"] = (
            aws_sdk_migration_hub_refactor_spaces.types.error_response.serialize_json(
                value["error"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    if "created_time" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.timestamp

        out["CreatedTime"] = (
            aws_sdk_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["created_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "CreatedByAccountId" in data:
        out["created_by_account_id"] = data["CreatedByAccountId"]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "ProxyType" in data:
        out["proxy_type"] = data["ProxyType"]
    if "ApiGatewayProxy" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_config

        out["api_gateway_proxy"] = (
            aws_sdk_migration_hub_refactor_spaces.types.api_gateway_proxy_config.deserialize_json(
                data["ApiGatewayProxy"]
            )
        )
    if "State" in data:
        out["state"] = data["State"]
    if "Tags" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = (
            aws_sdk_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
                data["Tags"]
            )
        )
    if "Error" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.error_response

        out["error"] = (
            aws_sdk_migration_hub_refactor_spaces.types.error_response.deserialize_json(
                data["Error"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if "CreatedTime" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.timestamp

        out["created_time"] = (
            aws_sdk_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["CreatedTime"]
            )
        )
    return out
