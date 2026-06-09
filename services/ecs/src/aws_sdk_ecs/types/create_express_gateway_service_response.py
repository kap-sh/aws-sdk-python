"""Generated from Smithy shape ``com.amazonaws.ecs#CreateExpressGatewayServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ecs_express_gateway_service


class CreateExpressGatewayServiceResponse(TypedDict):
    service: NotRequired[
        "aws_sdk_ecs.types.ecs_express_gateway_service.ECSExpressGatewayService"
    ]
    """<p>The full description of your Express service following the create operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExpressGatewayServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_ecs.types.ecs_express_gateway_service

        out["service"] = (
            aws_sdk_ecs.types.ecs_express_gateway_service.serialize_aws_json_1_1(
                value["service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExpressGatewayServiceResponse:
    out: CreateExpressGatewayServiceResponse = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_ecs.types.ecs_express_gateway_service

        out["service"] = (
            aws_sdk_ecs.types.ecs_express_gateway_service.deserialize_aws_json_1_1(
                data["service"]
            )
        )
    return out
