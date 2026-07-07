"""Generated from Smithy shape ``com.amazonaws.billing#DeleteBillingViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_arn


class DeleteBillingViewRequest(TypedDict, closed=True):
    arn: "aws_sdk_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    force: "bool"
    """<p> If set to true, forces deletion of the billing view even if it has derived resources (e.g. other billing views or budgets). Use with caution as this may break dependent resources. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteBillingViewRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["force"] = value.get("force", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteBillingViewRequest:
    out: DeleteBillingViewRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteBillingViewRequest.arn required")
    if "force" in data:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
