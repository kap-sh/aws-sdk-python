"""Generated from Smithy shape ``com.amazonaws.iot#DescribeBillingGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.billing_group_arn
    import aws_sdk_iot.types.billing_group_id
    import aws_sdk_iot.types.billing_group_metadata
    import aws_sdk_iot.types.billing_group_name
    import aws_sdk_iot.types.billing_group_properties
    import aws_sdk_iot.types.version


class DescribeBillingGroupResponse(TypedDict):
    billing_group_name: NotRequired[
        "aws_sdk_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group.</p>"""
    billing_group_id: NotRequired["aws_sdk_iot.types.billing_group_id.BillingGroupId"]
    """<p>The ID of the billing group.</p>"""
    billing_group_arn: NotRequired[
        "aws_sdk_iot.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The ARN of the billing group.</p>"""
    version: "aws_sdk_iot.types.version.Version"
    """<p>The version of the billing group.</p>"""
    billing_group_properties: NotRequired[
        "aws_sdk_iot.types.billing_group_properties.BillingGroupProperties"
    ]
    """<p>The properties of the billing group.</p>"""
    billing_group_metadata: NotRequired[
        "aws_sdk_iot.types.billing_group_metadata.BillingGroupMetadata"
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
        import aws_sdk_iot.types.billing_group_properties

        out["billingGroupProperties"] = (
            aws_sdk_iot.types.billing_group_properties.serialize_json(
                value["billing_group_properties"]
            )
        )
    if "billing_group_metadata" in value:
        import aws_sdk_iot.types.billing_group_metadata

        out["billingGroupMetadata"] = (
            aws_sdk_iot.types.billing_group_metadata.serialize_json(
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
        import aws_sdk_iot.types.billing_group_properties

        out["billing_group_properties"] = (
            aws_sdk_iot.types.billing_group_properties.deserialize_json(
                data["billingGroupProperties"]
            )
        )
    if "billingGroupMetadata" in data:
        import aws_sdk_iot.types.billing_group_metadata

        out["billing_group_metadata"] = (
            aws_sdk_iot.types.billing_group_metadata.deserialize_json(
                data["billingGroupMetadata"]
            )
        )
    return out
