"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_config_arn
    import capo_sagemaker.types.endpoint_config_name
    import capo_sagemaker.types.timestamp


class EndpointConfigSummary(TypedDict, closed=True):
    endpoint_config_name: NotRequired[
        "capo_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The name of the endpoint configuration.</p>"""
    endpoint_config_arn: NotRequired[
        "capo_sagemaker.types.endpoint_config_arn.EndpointConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint configuration.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the endpoint configuration was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointConfigSummary) -> dict:
    out: dict = {}
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "endpoint_config_arn" in value:
        out["EndpointConfigArn"] = value["endpoint_config_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointConfigSummary:
    out: EndpointConfigSummary = {}  # type: ignore[typeddict-item]
    if "EndpointConfigName" in data:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if "EndpointConfigArn" in data:
        out["endpoint_config_arn"] = data["EndpointConfigArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
