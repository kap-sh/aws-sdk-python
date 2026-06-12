"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CreateServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.client_token
    import aws_sdk_migration_hub_refactor_spaces.types.description
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_input
    import aws_sdk_migration_hub_refactor_spaces.types.service_endpoint_type
    import aws_sdk_migration_hub_refactor_spaces.types.service_name
    import aws_sdk_migration_hub_refactor_spaces.types.tag_map
    import aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_input
    import aws_sdk_migration_hub_refactor_spaces.types.vpc_id


class CreateServiceRequest(TypedDict):
    name: "aws_sdk_migration_hub_refactor_spaces.types.service_name.ServiceName"
    """<p>The name of the service.</p>"""
    description: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.description.Description"
    ]
    """<p>The description of the service.</p>"""
    environment_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment in which the service is created.</p>"""
    application_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p>The ID of the application which the service is created.</p>"""
    vpc_id: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    endpoint_type: "aws_sdk_migration_hub_refactor_spaces.types.service_endpoint_type.ServiceEndpointType"
    """<p>The type of endpoint to use for the service. The type can be a URL in a VPC or an Lambda function.</p>"""
    url_endpoint: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_input.UrlEndpointInput"
    ]
    """<p>The configuration for the URL endpoint type. When creating a route to a service, Refactor Spaces automatically resolves the address in the <code>UrlEndpointInput</code> object URL when the Domain Name System (DNS) time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds.</p>"""
    lambda_endpoint: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_input.LambdaEndpointInput"
    ]
    """<p>The configuration for the Lambda endpoint type.</p>"""
    tags: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags to assign to the service. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.. </p>"""
    client_token: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    out["EndpointType"] = value["endpoint_type"]
    if "url_endpoint" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_input

        out["UrlEndpoint"] = (
            aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_input.serialize_json(
                value["url_endpoint"]
            )
        )
    if "lambda_endpoint" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_input

        out["LambdaEndpoint"] = (
            aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_input.serialize_json(
                value["lambda_endpoint"]
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


def deserialize_json(data: dict) -> CreateServiceRequest:
    out: CreateServiceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateServiceRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "EndpointType" in data:
        out["endpoint_type"] = data["EndpointType"]
    else:
        raise DeserializationError("CreateServiceRequest.endpoint_type required")
    if "UrlEndpoint" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_input

        out["url_endpoint"] = (
            aws_sdk_migration_hub_refactor_spaces.types.url_endpoint_input.deserialize_json(
                data["UrlEndpoint"]
            )
        )
    if "LambdaEndpoint" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_input

        out["lambda_endpoint"] = (
            aws_sdk_migration_hub_refactor_spaces.types.lambda_endpoint_input.deserialize_json(
                data["LambdaEndpoint"]
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
