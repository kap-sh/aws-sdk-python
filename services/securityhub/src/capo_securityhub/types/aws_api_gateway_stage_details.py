"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayStageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_api_gateway_access_log_settings
    import capo_securityhub.types.aws_api_gateway_canary_settings
    import capo_securityhub.types.aws_api_gateway_method_settings_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.field_map
    import capo_securityhub.types.non_empty_string


class AwsApiGatewayStageDetails(TypedDict, closed=True):
    deployment_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the deployment that the stage points to.</p>"""
    client_certificate_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the client certificate for the stage.</p>"""
    stage_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the stage.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the stage.</p>"""
    cache_cluster_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether a cache cluster is enabled for the stage.</p>"""
    cache_cluster_size: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>If a cache cluster is enabled, the size of the cache cluster.</p>"""
    cache_cluster_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>If a cache cluster is enabled, the status of the cache cluster.</p>"""
    method_settings: NotRequired[
        "capo_securityhub.types.aws_api_gateway_method_settings_list.AwsApiGatewayMethodSettingsList"
    ]
    """<p>Defines the method settings for the stage.</p>"""
    variables: NotRequired["capo_securityhub.types.field_map.FieldMap"]
    """<p>A map that defines the stage variables for the stage.</p> <p>Variable names can have alphanumeric and underscore characters.</p> <p>Variable values can contain the following characters:</p> <ul> <li> <p>Uppercase and lowercase letters</p> </li> <li> <p>Numbers</p> </li> <li> <p>Special characters -._~:/?#&=,</p> </li> </ul>"""
    documentation_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the API documentation that is associated with the stage.</p>"""
    access_log_settings: NotRequired[
        "capo_securityhub.types.aws_api_gateway_access_log_settings.AwsApiGatewayAccessLogSettings"
    ]
    """<p>Settings for logging access for the stage.</p>"""
    canary_settings: NotRequired[
        "capo_securityhub.types.aws_api_gateway_canary_settings.AwsApiGatewayCanarySettings"
    ]
    """<p>Information about settings for canary deployment in the stage.</p>"""
    tracing_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether active tracing with X-Ray is enabled for the stage.</p>"""
    created_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    r"""<p>Indicates when the stage was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    last_updated_date: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the stage was most recently updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    web_acl_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the web ACL associated with the stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayStageDetails) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "client_certificate_id" in value:
        out["ClientCertificateId"] = value["client_certificate_id"]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "cache_cluster_enabled" in value:
        out["CacheClusterEnabled"] = value["cache_cluster_enabled"]
    if "cache_cluster_size" in value:
        out["CacheClusterSize"] = value["cache_cluster_size"]
    if "cache_cluster_status" in value:
        out["CacheClusterStatus"] = value["cache_cluster_status"]
    if "method_settings" in value:
        import capo_securityhub.types.aws_api_gateway_method_settings_list

        out["MethodSettings"] = (
            capo_securityhub.types.aws_api_gateway_method_settings_list.serialize_json(
                value["method_settings"]
            )
        )
    if "variables" in value:
        import capo_securityhub.types.field_map

        out["Variables"] = capo_securityhub.types.field_map.serialize_json(
            value["variables"]
        )
    if "documentation_version" in value:
        out["DocumentationVersion"] = value["documentation_version"]
    if "access_log_settings" in value:
        import capo_securityhub.types.aws_api_gateway_access_log_settings

        out["AccessLogSettings"] = (
            capo_securityhub.types.aws_api_gateway_access_log_settings.serialize_json(
                value["access_log_settings"]
            )
        )
    if "canary_settings" in value:
        import capo_securityhub.types.aws_api_gateway_canary_settings

        out["CanarySettings"] = (
            capo_securityhub.types.aws_api_gateway_canary_settings.serialize_json(
                value["canary_settings"]
            )
        )
    if "tracing_enabled" in value:
        out["TracingEnabled"] = value["tracing_enabled"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    if "last_updated_date" in value:
        out["LastUpdatedDate"] = value["last_updated_date"]
    if "web_acl_arn" in value:
        out["WebAclArn"] = value["web_acl_arn"]
    return out


def deserialize_json(data: dict) -> AwsApiGatewayStageDetails:
    out: AwsApiGatewayStageDetails = {}  # type: ignore[typeddict-item]
    if "DeploymentId" in data:
        out["deployment_id"] = data["DeploymentId"]
    if "ClientCertificateId" in data:
        out["client_certificate_id"] = data["ClientCertificateId"]
    if "StageName" in data:
        out["stage_name"] = data["StageName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CacheClusterEnabled" in data:
        out["cache_cluster_enabled"] = data["CacheClusterEnabled"]
    if "CacheClusterSize" in data:
        out["cache_cluster_size"] = data["CacheClusterSize"]
    if "CacheClusterStatus" in data:
        out["cache_cluster_status"] = data["CacheClusterStatus"]
    if "MethodSettings" in data:
        import capo_securityhub.types.aws_api_gateway_method_settings_list

        out["method_settings"] = (
            capo_securityhub.types.aws_api_gateway_method_settings_list.deserialize_json(
                data["MethodSettings"]
            )
        )
    if "Variables" in data:
        import capo_securityhub.types.field_map

        out["variables"] = capo_securityhub.types.field_map.deserialize_json(
            data["Variables"]
        )
    if "DocumentationVersion" in data:
        out["documentation_version"] = data["DocumentationVersion"]
    if "AccessLogSettings" in data:
        import capo_securityhub.types.aws_api_gateway_access_log_settings

        out["access_log_settings"] = (
            capo_securityhub.types.aws_api_gateway_access_log_settings.deserialize_json(
                data["AccessLogSettings"]
            )
        )
    if "CanarySettings" in data:
        import capo_securityhub.types.aws_api_gateway_canary_settings

        out["canary_settings"] = (
            capo_securityhub.types.aws_api_gateway_canary_settings.deserialize_json(
                data["CanarySettings"]
            )
        )
    if "TracingEnabled" in data:
        out["tracing_enabled"] = data["TracingEnabled"]
    if "CreatedDate" in data:
        out["created_date"] = data["CreatedDate"]
    if "LastUpdatedDate" in data:
        out["last_updated_date"] = data["LastUpdatedDate"]
    if "WebAclArn" in data:
        out["web_acl_arn"] = data["WebAclArn"]
    return out
