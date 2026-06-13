"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewHealthStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_status
    import aws_sdk_billing.types.billing_view_status_reasons


class BillingViewHealthStatus(TypedDict):
    status_code: NotRequired[
        "aws_sdk_billing.types.billing_view_status.BillingViewStatus"
    ]
    """<p>The current health status code of the billing view.</p>"""
    status_reasons: NotRequired[
        "aws_sdk_billing.types.billing_view_status_reasons.BillingViewStatusReasons"
    ]
    """<p>A list of reasons explaining the current health status, if applicable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewHealthStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_billing.types.billing_view_status

        out["statusCode"] = (
            aws_sdk_billing.types.billing_view_status.serialize_aws_json_1_0(
                value["status_code"]
            )
        )
    if "status_reasons" in value:
        import aws_sdk_billing.types.billing_view_status_reasons

        out["statusReasons"] = (
            aws_sdk_billing.types.billing_view_status_reasons.serialize_aws_json_1_0(
                value["status_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingViewHealthStatus:
    out: BillingViewHealthStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        import aws_sdk_billing.types.billing_view_status

        out["status_code"] = (
            aws_sdk_billing.types.billing_view_status.deserialize_aws_json_1_0(
                data["statusCode"]
            )
        )
    if "statusReasons" in data:
        import aws_sdk_billing.types.billing_view_status_reasons

        out["status_reasons"] = (
            aws_sdk_billing.types.billing_view_status_reasons.deserialize_aws_json_1_0(
                data["statusReasons"]
            )
        )
    return out
