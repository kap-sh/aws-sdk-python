"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__boolean
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.access_log_settings
    import capo_apigatewayv2.types.id
    import capo_apigatewayv2.types.route_settings
    import capo_apigatewayv2.types.route_settings_map
    import capo_apigatewayv2.types.stage_variables_map
    import capo_apigatewayv2.types.string_with_length_between0_and1024


class UpdateStageRequest(TypedDict, closed=True):
    access_log_settings: NotRequired[
        "capo_apigatewayv2.types.access_log_settings.AccessLogSettings"
    ]
    """<p>Settings for logging access in this stage.</p>"""
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    auto_deploy: NotRequired["capo_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether updates to an API automatically trigger a new deployment. The default value is false.</p>"""
    client_certificate_id: NotRequired["capo_apigatewayv2.types.id.Id"]
    """<p>The identifier of a client certificate for a Stage.</p>"""
    default_route_settings: NotRequired[
        "capo_apigatewayv2.types.route_settings.RouteSettings"
    ]
    """<p>The default route settings for the stage.</p>"""
    deployment_id: NotRequired["capo_apigatewayv2.types.id.Id"]
    """<p>The deployment identifier for the API stage. Can't be updated if autoDeploy is enabled.</p>"""
    description: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>The description for the API stage.</p>"""
    route_settings: NotRequired[
        "capo_apigatewayv2.types.route_settings_map.RouteSettingsMap"
    ]
    """<p>Route settings for the stage.</p>"""
    stage_name: "capo_apigatewayv2.types.__string.__string"
    """<p>The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters.</p>"""
    stage_variables: NotRequired[
        "capo_apigatewayv2.types.stage_variables_map.StageVariablesMap"
    ]
    """<p>A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&amp;=,]+.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStageRequest) -> dict:
    out: dict = {}
    if "access_log_settings" in value:
        import capo_apigatewayv2.types.access_log_settings

        out["accessLogSettings"] = (
            capo_apigatewayv2.types.access_log_settings.serialize_json(
                value["access_log_settings"]
            )
        )
    if "auto_deploy" in value:
        out["autoDeploy"] = value["auto_deploy"]
    if "client_certificate_id" in value:
        out["clientCertificateId"] = value["client_certificate_id"]
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
    if "route_settings" in value:
        import capo_apigatewayv2.types.route_settings_map

        out["routeSettings"] = (
            capo_apigatewayv2.types.route_settings_map.serialize_json(
                value["route_settings"]
            )
        )
    if "stage_variables" in value:
        import capo_apigatewayv2.types.stage_variables_map

        out["stageVariables"] = (
            capo_apigatewayv2.types.stage_variables_map.serialize_json(
                value["stage_variables"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateStageRequest:
    out: UpdateStageRequest = {}  # type: ignore[typeddict-item]
    if "accessLogSettings" in data:
        import capo_apigatewayv2.types.access_log_settings

        out["access_log_settings"] = (
            capo_apigatewayv2.types.access_log_settings.deserialize_json(
                data["accessLogSettings"]
            )
        )
    if "autoDeploy" in data:
        out["auto_deploy"] = data["autoDeploy"]
    if "clientCertificateId" in data:
        out["client_certificate_id"] = data["clientCertificateId"]
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
    if "routeSettings" in data:
        import capo_apigatewayv2.types.route_settings_map

        out["route_settings"] = (
            capo_apigatewayv2.types.route_settings_map.deserialize_json(
                data["routeSettings"]
            )
        )
    if "stageVariables" in data:
        import capo_apigatewayv2.types.stage_variables_map

        out["stage_variables"] = (
            capo_apigatewayv2.types.stage_variables_map.deserialize_json(
                data["stageVariables"]
            )
        )
    return out
