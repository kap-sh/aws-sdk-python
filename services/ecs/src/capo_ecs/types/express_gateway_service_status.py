"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.express_gateway_service_status_code
    import capo_ecs.types.string


class ExpressGatewayServiceStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "capo_ecs.types.express_gateway_service_status_code.ExpressGatewayServiceStatusCode"
    ]
    """<p>The status of the Express service.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>Information about why the Express service is in the current status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import capo_ecs.types.express_gateway_service_status_code

        out["statusCode"] = (
            capo_ecs.types.express_gateway_service_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayServiceStatus:
    out: ExpressGatewayServiceStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        import capo_ecs.types.express_gateway_service_status_code

        out["status_code"] = (
            capo_ecs.types.express_gateway_service_status_code.deserialize_aws_json_1_1(
                data["statusCode"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
