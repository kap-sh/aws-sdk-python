"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_service_status_code
    import aws_sdk_ecs.types.string


class ExpressGatewayServiceStatus(TypedDict):
    status_code: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_status_code.ExpressGatewayServiceStatusCode"
    ]
    """<p>The status of the Express service.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the Express service is in the current status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_ecs.types.express_gateway_service_status_code

        out["statusCode"] = (
            aws_sdk_ecs.types.express_gateway_service_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayServiceStatus:
    out: ExpressGatewayServiceStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        import aws_sdk_ecs.types.express_gateway_service_status_code

        out["status_code"] = (
            aws_sdk_ecs.types.express_gateway_service_status_code.deserialize_aws_json_1_1(
                data["statusCode"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
