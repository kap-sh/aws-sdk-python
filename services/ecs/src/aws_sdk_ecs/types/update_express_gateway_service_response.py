"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateExpressGatewayServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.updated_express_gateway_service


class UpdateExpressGatewayServiceResponse(TypedDict, closed=True):
    service: NotRequired[
        "aws_sdk_ecs.types.updated_express_gateway_service.UpdatedExpressGatewayService"
    ]
    """<p>The full description of your express gateway service following the update call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExpressGatewayServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_ecs.types.updated_express_gateway_service

        out["service"] = (
            aws_sdk_ecs.types.updated_express_gateway_service.serialize_aws_json_1_1(
                value["service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExpressGatewayServiceResponse:
    out: UpdateExpressGatewayServiceResponse = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_ecs.types.updated_express_gateway_service

        out["service"] = (
            aws_sdk_ecs.types.updated_express_gateway_service.deserialize_aws_json_1_1(
                data["service"]
            )
        )
    return out
