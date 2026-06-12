"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioUsageModificationError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error_code
    import aws_sdk_bcm_pricing_calculator.types.key

class BatchCreateBillScenarioUsageModificationError(TypedDict):
    key: NotRequired["aws_sdk_bcm_pricing_calculator.types.key.Key"]
    """<p> The key of the entry that caused the error. </p>"""
    error_message: NotRequired["str"]
    """<p> A descriptive message for the error that occurred. </p>"""
    error_code: NotRequired["aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error_code.BatchCreateBillScenarioUsageModificationErrorCode"]
    """<p> The error code associated with the failed operation. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillScenarioUsageModificationError) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error_code
        out["errorCode"] = aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error_code.serialize_aws_json_1_0(value["error_code"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillScenarioUsageModificationError:
    out: BatchCreateBillScenarioUsageModificationError = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error_code
        out["error_code"] = aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_error_code.deserialize_aws_json_1_0(data["errorCode"])
    return out