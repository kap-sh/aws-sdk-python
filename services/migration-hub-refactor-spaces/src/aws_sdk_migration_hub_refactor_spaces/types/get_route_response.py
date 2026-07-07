"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetRouteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.account_id
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.boolean
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.error_response
    import aws_sdk_migration_hub_refactor_spaces.types.http_methods
    import aws_sdk_migration_hub_refactor_spaces.types.path_resource_to_id
    import aws_sdk_migration_hub_refactor_spaces.types.resource_arn
    import aws_sdk_migration_hub_refactor_spaces.types.route_id
    import aws_sdk_migration_hub_refactor_spaces.types.route_state
    import aws_sdk_migration_hub_refactor_spaces.types.route_type
    import aws_sdk_migration_hub_refactor_spaces.types.service_id
    import aws_sdk_migration_hub_refactor_spaces.types.tag_map
    import aws_sdk_migration_hub_refactor_spaces.types.timestamp
    import aws_sdk_migration_hub_refactor_spaces.types.uri_path


class GetRouteResponse(TypedDict, closed=True):
    route_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_id.RouteId"
    ]
    """<p>The unique identifier of the route.</p> <p> <b>DEFAULT</b>: All traffic that does not match another route is forwarded to the default route. Applications must have a default route before any other routes can be created.</p> <p> <b>URI_PATH</b>: A route that is based on a URI path.</p>"""
    arn: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the route.</p>"""
    owner_account_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the route owner.</p>"""
    created_by_account_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the route creator.</p>"""
    route_type: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_type.RouteType"
    ]
    """<p>The type of route.</p>"""
    service_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.service_id.ServiceId"
    ]
    """<p>The unique identifier of the service.</p>"""
    application_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The ID of the application that the route belongs to. </p>"""
    environment_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>Unique identifier of the environment.</p>"""
    source_path: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.uri_path.UriPath"
    ]
    """<p>This is the path that Refactor Spaces uses to match traffic. Paths must start with <code>/</code> and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.</p>"""
    methods: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.http_methods.HttpMethods"
    ]
    """<p>A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service. </p>"""
    include_child_paths: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.boolean.Boolean"
    ]
    """<p>Indicates whether to match all subpaths of the given source path. If this value is <code>false</code>, requests must match the source path exactly before they are forwarded to this route's service. </p>"""
    path_resource_to_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.path_resource_to_id.PathResourceToId"
    ]
    """<p>A mapping of Amazon API Gateway path resources to resource IDs. </p>"""
    state: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_state.RouteState"
    ]
    """<p>The current state of the route. </p>"""
    tags: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags assigned to the route. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair. </p>"""
    error: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.error_response.ErrorResponse"
    ]
    """<p>Any error associated with the route resource. </p>"""
    last_updated_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the route was last updated. </p>"""
    created_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of when the route is created. </p>"""
    append_source_path: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.boolean.Boolean"
    ]
    """<p>If set to <code>true</code>, this option appends the source path to the service URL endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteResponse) -> dict:
    out: dict = {}
    if "route_id" in value:
        out["RouteId"] = value["route_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "created_by_account_id" in value:
        out["CreatedByAccountId"] = value["created_by_account_id"]
    if "route_type" in value:
        out["RouteType"] = value["route_type"]
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "source_path" in value:
        out["SourcePath"] = value["source_path"]
    if "methods" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.http_methods

        out["Methods"] = (
            aws_sdk_migration_hub_refactor_spaces.types.http_methods.serialize_json(
                value["methods"]
            )
        )
    if "include_child_paths" in value:
        out["IncludeChildPaths"] = value["include_child_paths"]
    if "path_resource_to_id" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.path_resource_to_id

        out["PathResourceToId"] = (
            aws_sdk_migration_hub_refactor_spaces.types.path_resource_to_id.serialize_json(
                value["path_resource_to_id"]
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
    if "append_source_path" in value:
        out["AppendSourcePath"] = value["append_source_path"]
    return out


def deserialize_json(data: dict) -> GetRouteResponse:
    out: GetRouteResponse = {}  # type: ignore[typeddict-item]
    if "RouteId" in data:
        out["route_id"] = data["RouteId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "CreatedByAccountId" in data:
        out["created_by_account_id"] = data["CreatedByAccountId"]
    if "RouteType" in data:
        out["route_type"] = data["RouteType"]
    if "ServiceId" in data:
        out["service_id"] = data["ServiceId"]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "SourcePath" in data:
        out["source_path"] = data["SourcePath"]
    if "Methods" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.http_methods

        out["methods"] = (
            aws_sdk_migration_hub_refactor_spaces.types.http_methods.deserialize_json(
                data["Methods"]
            )
        )
    if "IncludeChildPaths" in data:
        out["include_child_paths"] = data["IncludeChildPaths"]
    if "PathResourceToId" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.path_resource_to_id

        out["path_resource_to_id"] = (
            aws_sdk_migration_hub_refactor_spaces.types.path_resource_to_id.deserialize_json(
                data["PathResourceToId"]
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
    if "AppendSourcePath" in data:
        out["append_source_path"] = data["AppendSourcePath"]
    return out
