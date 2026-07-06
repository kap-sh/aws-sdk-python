"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeEndpointConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_config_name


class DescribeEndpointConfigInput(TypedDict, closed=True):
    endpoint_config_name: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The name of the endpoint configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointConfigInput) -> dict:
    out: dict = {}
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointConfigInput:
    out: DescribeEndpointConfigInput = {}  # type: ignore[typeddict-item]
    if "EndpointConfigName" in data:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    return out
