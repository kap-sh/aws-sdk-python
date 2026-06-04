"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteExpressGatewayServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ecs_express_gateway_service


class DeleteExpressGatewayServiceResponse(TypedDict):
    service: NotRequired[
        "aws_sdk_ecs.types.ecs_express_gateway_service.ECSExpressGatewayService"
    ]
    """<p>The full description of the deleted express service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExpressGatewayServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_ecs.types.ecs_express_gateway_service

        out["service"] = (
            aws_sdk_ecs.types.ecs_express_gateway_service.serialize_aws_json_1_1(
                value["service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExpressGatewayServiceResponse:
    out: DeleteExpressGatewayServiceResponse = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_ecs.types.ecs_express_gateway_service

        out["service"] = (
            aws_sdk_ecs.types.ecs_express_gateway_service.deserialize_aws_json_1_1(
                data["service"]
            )
        )
    return out
