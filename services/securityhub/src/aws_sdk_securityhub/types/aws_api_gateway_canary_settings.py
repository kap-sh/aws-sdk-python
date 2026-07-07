"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayCanarySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.double
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.non_empty_string


class AwsApiGatewayCanarySettings(TypedDict, closed=True):
    percent_traffic: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p>The percentage of traffic that is diverted to a canary deployment.</p>"""
    deployment_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The deployment identifier for the canary deployment.</p>"""
    stage_variable_overrides: NotRequired[
        "aws_sdk_securityhub.types.field_map.FieldMap"
    ]
    """<p>Stage variables that are overridden in the canary release deployment. The variables include new stage variables that are introduced in the canary.</p> <p>Each variable is represented as a string-to-string map between the stage variable name and the variable value.</p>"""
    use_stage_cache: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the canary deployment uses the stage cache.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayCanarySettings) -> dict:
    out: dict = {}
    if "percent_traffic" in value:
        out["PercentTraffic"] = value["percent_traffic"]
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "stage_variable_overrides" in value:
        import aws_sdk_securityhub.types.field_map

        out["StageVariableOverrides"] = (
            aws_sdk_securityhub.types.field_map.serialize_json(
                value["stage_variable_overrides"]
            )
        )
    if "use_stage_cache" in value:
        out["UseStageCache"] = value["use_stage_cache"]
    return out


def deserialize_json(data: dict) -> AwsApiGatewayCanarySettings:
    out: AwsApiGatewayCanarySettings = {}  # type: ignore[typeddict-item]
    if "PercentTraffic" in data:
        out["percent_traffic"] = data["PercentTraffic"]
    if "DeploymentId" in data:
        out["deployment_id"] = data["DeploymentId"]
    if "StageVariableOverrides" in data:
        import aws_sdk_securityhub.types.field_map

        out["stage_variable_overrides"] = (
            aws_sdk_securityhub.types.field_map.deserialize_json(
                data["StageVariableOverrides"]
            )
        )
    if "UseStageCache" in data:
        out["use_stage_cache"] = data["UseStageCache"]
    return out
