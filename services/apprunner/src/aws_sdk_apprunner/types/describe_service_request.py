"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn


class DescribeServiceRequest(TypedDict, closed=True):
    service_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service that you want a description for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeServiceRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeServiceRequest:
    out: DescribeServiceRequest = {}  # type: ignore[typeddict-item]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    else:
        raise DeserializationError("DescribeServiceRequest.service_arn required")
    return out
