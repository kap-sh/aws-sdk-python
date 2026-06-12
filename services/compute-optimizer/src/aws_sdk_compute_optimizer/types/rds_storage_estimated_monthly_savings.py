"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSStorageEstimatedMonthlySavings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.currency
    import aws_sdk_compute_optimizer.types.value


class RDSStorageEstimatedMonthlySavings(TypedDict):
    currency: NotRequired["aws_sdk_compute_optimizer.types.currency.Currency"]
    """<p> The currency of the estimated monthly savings. </p>"""
    value: "aws_sdk_compute_optimizer.types.value.Value"
    """<p> The value of the estimated monthly savings for DB instance storage. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSStorageEstimatedMonthlySavings) -> dict:
    out: dict = {}
    if "currency" in value:
        import aws_sdk_compute_optimizer.types.currency

        out["currency"] = (
            aws_sdk_compute_optimizer.types.currency.serialize_aws_json_1_0(
                value["currency"]
            )
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSStorageEstimatedMonthlySavings:
    out: RDSStorageEstimatedMonthlySavings = {}  # type: ignore[typeddict-item]
    if "currency" in data:
        import aws_sdk_compute_optimizer.types.currency

        out["currency"] = (
            aws_sdk_compute_optimizer.types.currency.deserialize_aws_json_1_0(
                data["currency"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
