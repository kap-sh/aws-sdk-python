"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#CreateBillEstimateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_name
    import aws_sdk_bcm_pricing_calculator.types.client_token
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.tags


class CreateBillEstimateRequest(TypedDict, closed=True):
    bill_scenario_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to create a Bill estimate. </p>"""
    name: "aws_sdk_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
    """<p> The name of the Bill estimate that will be created. Names must be unique for an account. </p>"""
    client_token: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""
    tags: NotRequired["aws_sdk_bcm_pricing_calculator.types.tags.Tags"]
    """<p> An optional list of tags to associate with the specified BillEstimate. You can use resource tags to control access to your BillEstimate using IAM policies. Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags: </p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services. </p> </li> <li> <p>The maximum length of a key is 128 characters.</p> </li> <li> <p>The maximum length of a value is 256 characters.</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code>.</p> </li> <li> <p>Keys and values are case sensitive.</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBillEstimateRequest) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_bcm_pricing_calculator.types.tags

        out["tags"] = aws_sdk_bcm_pricing_calculator.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBillEstimateRequest:
    out: CreateBillEstimateRequest = {}  # type: ignore[typeddict-item]
    if "billScenarioId" in data:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        raise DeserializationError(
            "CreateBillEstimateRequest.bill_scenario_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateBillEstimateRequest.name required")
    if "tags" in data:
        import aws_sdk_bcm_pricing_calculator.types.tags

        out["tags"] = (
            aws_sdk_bcm_pricing_calculator.types.tags.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
