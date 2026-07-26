"""Generated from Smithy shape ``com.amazonaws.iot#DescribeBillingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.billing_group_arn
    import capo_iot.types.billing_group_id
    import capo_iot.types.billing_group_metadata
    import capo_iot.types.billing_group_name
    import capo_iot.types.billing_group_properties
    import capo_iot.types.version


class DescribeBillingGroupResponse(TypedDict, closed=True):
    billing_group_name: NotRequired[
        "capo_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group.</p>"""
    billing_group_id: NotRequired["capo_iot.types.billing_group_id.BillingGroupId"]
    """<p>The ID of the billing group.</p>"""
    billing_group_arn: NotRequired["capo_iot.types.billing_group_arn.BillingGroupArn"]
    """<p>The ARN of the billing group.</p>"""
    version: "capo_iot.types.version.Version"
    """<p>The version of the billing group.</p>"""
    billing_group_properties: NotRequired[
        "capo_iot.types.billing_group_properties.BillingGroupProperties"
    ]
    """<p>The properties of the billing group.</p>"""
    billing_group_metadata: NotRequired[
        "capo_iot.types.billing_group_metadata.BillingGroupMetadata"
    ]
    """<p>Additional information about the billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBillingGroupResponse) -> dict:
    out: dict = {}
    if "billing_group_name" in value:
        out["billingGroupName"] = value["billing_group_name"]
    if "billing_group_id" in value:
        out["billingGroupId"] = value["billing_group_id"]
    if "billing_group_arn" in value:
        out["billingGroupArn"] = value["billing_group_arn"]
    out["version"] = value.get("version", 0)
    if "billing_group_properties" in value:
        import capo_iot.types.billing_group_properties

        out["billingGroupProperties"] = (
            capo_iot.types.billing_group_properties.serialize_json(
                value["billing_group_properties"]
            )
        )
    if "billing_group_metadata" in value:
        import capo_iot.types.billing_group_metadata

        out["billingGroupMetadata"] = (
            capo_iot.types.billing_group_metadata.serialize_json(
                value["billing_group_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeBillingGroupResponse:
    out: DescribeBillingGroupResponse = {}  # type: ignore[typeddict-item]
    if "billingGroupName" in data:
        out["billing_group_name"] = data["billingGroupName"]
    if "billingGroupId" in data:
        out["billing_group_id"] = data["billingGroupId"]
    if "billingGroupArn" in data:
        out["billing_group_arn"] = data["billingGroupArn"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if "billingGroupProperties" in data:
        import capo_iot.types.billing_group_properties

        out["billing_group_properties"] = (
            capo_iot.types.billing_group_properties.deserialize_json(
                data["billingGroupProperties"]
            )
        )
    if "billingGroupMetadata" in data:
        import capo_iot.types.billing_group_metadata

        out["billing_group_metadata"] = (
            capo_iot.types.billing_group_metadata.deserialize_json(
                data["billingGroupMetadata"]
            )
        )
    return out
