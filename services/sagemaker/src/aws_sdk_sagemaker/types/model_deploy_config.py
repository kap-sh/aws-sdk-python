"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDeployConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_generate_endpoint_name
    import aws_sdk_sagemaker.types.endpoint_name


class ModelDeployConfig(TypedDict, closed=True):
    auto_generate_endpoint_name: NotRequired[
        "aws_sdk_sagemaker.types.auto_generate_endpoint_name.AutoGenerateEndpointName"
    ]
    """<p>Set to <code>True</code> to automatically generate an endpoint name for a one-click Autopilot model deployment; set to <code>False</code> otherwise. The default value is <code>False</code>.</p> <note> <p>If you set <code>AutoGenerateEndpointName</code> to <code>True</code>, do not specify the <code>EndpointName</code>; otherwise a 400 error is thrown.</p> </note>"""
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>Specifies the endpoint name to use for a one-click Autopilot model deployment if the endpoint name is not generated automatically.</p> <note> <p>Specify the <code>EndpointName</code> if and only if you set <code>AutoGenerateEndpointName</code> to <code>False</code>; otherwise a 400 error is thrown.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDeployConfig) -> dict:
    out: dict = {}
    if "auto_generate_endpoint_name" in value:
        out["AutoGenerateEndpointName"] = value["auto_generate_endpoint_name"]
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDeployConfig:
    out: ModelDeployConfig = {}  # type: ignore[typeddict-item]
    if "AutoGenerateEndpointName" in data:
        out["auto_generate_endpoint_name"] = data["AutoGenerateEndpointName"]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    return out
