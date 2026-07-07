"""Generated from Smithy shape ``com.amazonaws.pricing#GetAttributeValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pricing.types.attribute_value_list
    import aws_sdk_pricing.types.string


class GetAttributeValuesResponse(TypedDict, closed=True):
    attribute_values: NotRequired[
        "aws_sdk_pricing.types.attribute_value_list.AttributeValueList"
    ]
    """<p>The list of values for an attribute. For example, <code>Throughput Optimized HDD</code> and <code>Provisioned IOPS</code> are two available values for the <code>AmazonEC2</code> <code>volumeType</code>.</p>"""
    next_token: NotRequired["aws_sdk_pricing.types.string.String"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAttributeValuesResponse) -> dict:
    out: dict = {}
    if "attribute_values" in value:
        import aws_sdk_pricing.types.attribute_value_list

        out["AttributeValues"] = (
            aws_sdk_pricing.types.attribute_value_list.serialize_aws_json_1_1(
                value["attribute_values"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAttributeValuesResponse:
    out: GetAttributeValuesResponse = {}  # type: ignore[typeddict-item]
    if "AttributeValues" in data:
        import aws_sdk_pricing.types.attribute_value_list

        out["attribute_values"] = (
            aws_sdk_pricing.types.attribute_value_list.deserialize_aws_json_1_1(
                data["AttributeValues"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
