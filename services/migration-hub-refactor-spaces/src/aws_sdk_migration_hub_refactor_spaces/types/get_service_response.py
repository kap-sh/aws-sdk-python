"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.account_id
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.description
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.error_response
    import aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_config
    import aws_sdk_migration_hub_refactor_spaces.types.resource_arn
    import aws_sdk_migration_hub_refactor_spaces.types.service_endpoint_type
    import aws_sdk_migration_hub_refactor_spaces.types.service_id
    import aws_sdk_migration_hub_refactor_spaces.types.service_name
    import aws_sdk_migration_hub_refactor_spaces.types.service_state
    import aws_sdk_migration_hub_refactor_spaces.types.tag_map
    import aws_sdk_migration_hub_refactor_spaces.types.timestamp
    import aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_config
    import aws_sdk_migration_hub_refactor_spaces.types.vpc_id


class GetServiceResponse(TypedDict):
    service_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.service_id.ServiceId"
    ]
    """<p>The unique identifier of the service.</p>"""
    name: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.service_name.ServiceName"
    ]
    """<p>The name of the service.</p>"""
    arn: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    owner_account_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the service owner.</p>"""
    created_by_account_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the service creator.</p>"""
    description: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.description.Description"
    ]
    """<p>The description of the service. </p>"""
    environment_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The unique identifier of the environment.</p>"""
    application_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The ID of the application.</p>"""
    vpc_id: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.vpc_id.VpcId"]
    """<p>The ID of the virtual private cloud (VPC). </p>"""
    endpoint_type: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.service_endpoint_type.ServiceEndpointType"
    ]
    """<p>The endpoint type of the service.</p>"""
    url_endpoint: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_config.UrlEndpointConfig"
    ]
    """<p>The configuration for the URL endpoint type.</p> <p>The <b>Url</b> isthe URL of the endpoint type.</p> <p>The <b>HealthUrl</b> is the health check URL of the endpoint type. </p>"""
    lambda_endpoint: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_config.LambdaEndpointConfig"
    ]
    """<p>The configuration for the Lambda endpoint type.</p> <p>The <b>Arn</b> is the Amazon Resource Name (ARN) of the Lambda function associated with this service. </p>"""
    state: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.service_state.ServiceState"
    ]
    """<p>The current state of the service. </p>"""
    tags: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags assigned to the service. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair. </p>"""
    error: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.error_response.ErrorResponse"
    ]
    """<p>Any error associated with the service resource. </p>"""
    last_updated_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the service was last updated. </p>"""
    created_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of when the service is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceResponse) -> dict:
    out: dict = {}
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "created_by_account_id" in value:
        out["CreatedByAccountId"] = value["created_by_account_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "endpoint_type" in value:
        out["EndpointType"] = value["endpoint_type"]
    if "url_endpoint" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_config

        out["UrlEndpoint"] = (
            aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_config.serialize_json(
                value["url_endpoint"]
            )
        )
    if "lambda_endpoint" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_config

        out["LambdaEndpoint"] = (
            aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_config.serialize_json(
                value["lambda_endpoint"]
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


def deserialize_json(data: dict) -> GetServiceResponse:
    out: GetServiceResponse = {}  # type: ignore[typeddict-item]
    if "ServiceId" in data:
        out["service_id"] = data["ServiceId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "CreatedByAccountId" in data:
        out["created_by_account_id"] = data["CreatedByAccountId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "EndpointType" in data:
        out["endpoint_type"] = data["EndpointType"]
    if "UrlEndpoint" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_config

        out["url_endpoint"] = (
            aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_config.deserialize_json(
                data["UrlEndpoint"]
            )
        )
    if "LambdaEndpoint" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_config

        out["lambda_endpoint"] = (
            aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_config.deserialize_json(
                data["LambdaEndpoint"]
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
