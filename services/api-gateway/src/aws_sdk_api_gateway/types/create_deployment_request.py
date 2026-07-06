"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.cache_cluster_size
    import aws_sdk_api_gateway.types.deployment_canary_settings
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.nullable_boolean
    import aws_sdk_api_gateway.types.string


class CreateDeploymentRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The name of the Stage resource for the Deployment resource to create.</p>"""
    stage_description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of the Stage resource for the Deployment resource to create.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description for the Deployment resource to create.</p>"""
    cache_cluster_enabled: NotRequired[
        "aws_sdk_api_gateway.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Enables a cache cluster for the Stage resource specified in the input.</p>"""
    cache_cluster_size: NotRequired[
        "aws_sdk_api_gateway.types.cache_cluster_size.CacheClusterSize"
    ]
    r"""<p>The stage's cache capacity in GB. For more information about choosing a cache size, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html\">Enabling API caching to enhance responsiveness</a>.</p>"""
    variables: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A map that defines the stage variables for the Stage resource that is associated with the new deployment. Variable names can have alphanumeric and underscore characters, and the values must match <code>[A-Za-z0-9-._~:/?#&=,]+</code>.</p>"""
    canary_settings: NotRequired[
        "aws_sdk_api_gateway.types.deployment_canary_settings.DeploymentCanarySettings"
    ]
    """<p>The input configuration for the canary deployment when the deployment is a canary release deployment. </p>"""
    tracing_enabled: NotRequired[
        "aws_sdk_api_gateway.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether active tracing with X-ray is enabled for the Stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentRequest) -> dict:
    out: dict = {}
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "stage_description" in value:
        out["stageDescription"] = value["stage_description"]
    if "description" in value:
        out["description"] = value["description"]
    if "cache_cluster_enabled" in value:
        out["cacheClusterEnabled"] = value["cache_cluster_enabled"]
    if "cache_cluster_size" in value:
        import aws_sdk_api_gateway.types.cache_cluster_size

        out["cacheClusterSize"] = (
            aws_sdk_api_gateway.types.cache_cluster_size.serialize_json(
                value["cache_cluster_size"]
            )
        )
    if "variables" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["variables"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
                value["variables"]
            )
        )
    if "canary_settings" in value:
        import aws_sdk_api_gateway.types.deployment_canary_settings

        out["canarySettings"] = (
            aws_sdk_api_gateway.types.deployment_canary_settings.serialize_json(
                value["canary_settings"]
            )
        )
    if "tracing_enabled" in value:
        out["tracingEnabled"] = value["tracing_enabled"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentRequest:
    out: CreateDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    if "stageDescription" in data:
        out["stage_description"] = data["stageDescription"]
    if "description" in data:
        out["description"] = data["description"]
    if "cacheClusterEnabled" in data:
        out["cache_cluster_enabled"] = data["cacheClusterEnabled"]
    if "cacheClusterSize" in data:
        import aws_sdk_api_gateway.types.cache_cluster_size

        out["cache_cluster_size"] = (
            aws_sdk_api_gateway.types.cache_cluster_size.deserialize_json(
                data["cacheClusterSize"]
            )
        )
    if "variables" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["variables"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["variables"]
            )
        )
    if "canarySettings" in data:
        import aws_sdk_api_gateway.types.deployment_canary_settings

        out["canary_settings"] = (
            aws_sdk_api_gateway.types.deployment_canary_settings.deserialize_json(
                data["canarySettings"]
            )
        )
    if "tracingEnabled" in data:
        out["tracing_enabled"] = data["tracingEnabled"]
    return out
