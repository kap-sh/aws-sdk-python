"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Stage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__boolean
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.__timestamp_iso8601
    import capo_apigatewayv2.types.access_log_settings
    import capo_apigatewayv2.types.id
    import capo_apigatewayv2.types.route_settings
    import capo_apigatewayv2.types.route_settings_map
    import capo_apigatewayv2.types.stage_variables_map
    import capo_apigatewayv2.types.string_with_length_between0_and1024
    import capo_apigatewayv2.types.string_with_length_between1_and128
    import capo_apigatewayv2.types.tags


class Stage(TypedDict, closed=True):
    access_log_settings: NotRequired[
        "capo_apigatewayv2.types.access_log_settings.AccessLogSettings"
    ]
    """<p>Settings for logging access in this stage.</p>"""
    api_gateway_managed: NotRequired["capo_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether a stage is managed by API Gateway. If you created an API using quick create, the $default stage is managed by API Gateway. You can't modify the $default stage.</p>"""
    auto_deploy: NotRequired["capo_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether updates to an API automatically trigger a new deployment. The default value is false.</p>"""
    client_certificate_id: NotRequired["capo_apigatewayv2.types.id.Id"]
    """<p>The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.</p>"""
    created_date: NotRequired[
        "capo_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the stage was created.</p>"""
    default_route_settings: NotRequired[
        "capo_apigatewayv2.types.route_settings.RouteSettings"
    ]
    """<p>Default route settings for the stage.</p>"""
    deployment_id: NotRequired["capo_apigatewayv2.types.id.Id"]
    """<p>The identifier of the Deployment that the Stage is associated with. Can't be updated if autoDeploy is enabled.</p>"""
    description: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>The description of the stage.</p>"""
    last_deployment_status_message: NotRequired[
        "capo_apigatewayv2.types.__string.__string"
    ]
    """<p>Describes the status of the last deployment of a stage. Supported only for stages with autoDeploy enabled.</p>"""
    last_updated_date: NotRequired[
        "capo_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the stage was last updated.</p>"""
    route_settings: NotRequired[
        "capo_apigatewayv2.types.route_settings_map.RouteSettingsMap"
    ]
    """<p>Route settings for the stage, by routeKey.</p>"""
    stage_name: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the stage.</p>"""
    stage_variables: NotRequired[
        "capo_apigatewayv2.types.stage_variables_map.StageVariablesMap"
    ]
    """<p>A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&amp;=,]+.</p>"""
    tags: NotRequired["capo_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Stage) -> dict:
    out: dict = {}
    if "access_log_settings" in value:
        import capo_apigatewayv2.types.access_log_settings

        out["accessLogSettings"] = (
            capo_apigatewayv2.types.access_log_settings.serialize_json(
                value["access_log_settings"]
            )
        )
    if "api_gateway_managed" in value:
        out["apiGatewayManaged"] = value["api_gateway_managed"]
    if "auto_deploy" in value:
        out["autoDeploy"] = value["auto_deploy"]
    if "client_certificate_id" in value:
        out["clientCertificateId"] = value["client_certificate_id"]
    if "created_date" in value:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["createdDate"] = capo_apigatewayv2.types.__timestamp_iso8601.serialize_json(
            value["created_date"]
        )
    if "default_route_settings" in value:
        import capo_apigatewayv2.types.route_settings

        out["defaultRouteSettings"] = (
            capo_apigatewayv2.types.route_settings.serialize_json(
                value["default_route_settings"]
            )
        )
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "last_deployment_status_message" in value:
        out["lastDeploymentStatusMessage"] = value["last_deployment_status_message"]
    if "last_updated_date" in value:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["lastUpdatedDate"] = (
            capo_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["last_updated_date"]
            )
        )
    if "route_settings" in value:
        import capo_apigatewayv2.types.route_settings_map

        out["routeSettings"] = (
            capo_apigatewayv2.types.route_settings_map.serialize_json(
                value["route_settings"]
            )
        )
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "stage_variables" in value:
        import capo_apigatewayv2.types.stage_variables_map

        out["stageVariables"] = (
            capo_apigatewayv2.types.stage_variables_map.serialize_json(
                value["stage_variables"]
            )
        )
    if "tags" in value:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Stage:
    out: Stage = {}  # type: ignore[typeddict-item]
    if "accessLogSettings" in data:
        import capo_apigatewayv2.types.access_log_settings

        out["access_log_settings"] = (
            capo_apigatewayv2.types.access_log_settings.deserialize_json(
                data["accessLogSettings"]
            )
        )
    if "apiGatewayManaged" in data:
        out["api_gateway_managed"] = data["apiGatewayManaged"]
    if "autoDeploy" in data:
        out["auto_deploy"] = data["autoDeploy"]
    if "clientCertificateId" in data:
        out["client_certificate_id"] = data["clientCertificateId"]
    if "createdDate" in data:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["created_date"] = (
            capo_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["createdDate"]
            )
        )
    if "defaultRouteSettings" in data:
        import capo_apigatewayv2.types.route_settings

        out["default_route_settings"] = (
            capo_apigatewayv2.types.route_settings.deserialize_json(
                data["defaultRouteSettings"]
            )
        )
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "description" in data:
        out["description"] = data["description"]
    if "lastDeploymentStatusMessage" in data:
        out["last_deployment_status_message"] = data["lastDeploymentStatusMessage"]
    if "lastUpdatedDate" in data:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["last_updated_date"] = (
            capo_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "routeSettings" in data:
        import capo_apigatewayv2.types.route_settings_map

        out["route_settings"] = (
            capo_apigatewayv2.types.route_settings_map.deserialize_json(
                data["routeSettings"]
            )
        )
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    if "stageVariables" in data:
        import capo_apigatewayv2.types.stage_variables_map

        out["stage_variables"] = (
            capo_apigatewayv2.types.stage_variables_map.deserialize_json(
                data["stageVariables"]
            )
        )
    if "tags" in data:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
