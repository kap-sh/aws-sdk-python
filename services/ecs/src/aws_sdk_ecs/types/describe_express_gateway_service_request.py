"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_include_list
    import aws_sdk_ecs.types.string


class DescribeExpressGatewayServiceRequest(TypedDict):
    service_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Express service to describe. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>"""
    include: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_include_list.ExpressGatewayServiceIncludeList"
    ]
    """<p>Specifies additional information to include in the response. Valid values are <code>TAGS</code> to include resource tags associated with the Express service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExpressGatewayServiceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    if "include" in value:
        import aws_sdk_ecs.types.express_gateway_service_include_list

        out["include"] = (
            aws_sdk_ecs.types.express_gateway_service_include_list.serialize_aws_json_1_1(
                value["include"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExpressGatewayServiceRequest:
    out: DescribeExpressGatewayServiceRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "DescribeExpressGatewayServiceRequest.service_arn required"
        )
    if "include" in data:
        import aws_sdk_ecs.types.express_gateway_service_include_list

        out["include"] = (
            aws_sdk_ecs.types.express_gateway_service_include_list.deserialize_aws_json_1_1(
                data["include"]
            )
        )
    return out
