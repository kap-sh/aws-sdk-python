"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressesAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_attribute_name
    import aws_sdk_ec2.types.address_max_results
    import aws_sdk_ec2.types.allocation_ids
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.next_token


class DescribeAddressesAttributeRequest(TypedDict):
    allocation_ids: NotRequired["aws_sdk_ec2.types.allocation_ids.AllocationIds"]
    """<p>[EC2-VPC] The allocation IDs.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.address_attribute_name.AddressAttributeName"
    ]
    """<p>The attribute of the IP address.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.address_max_results.AddressMaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAddressesAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_ids" in value:
        import aws_sdk_ec2.types.allocation_ids

        aws_sdk_ec2.types.allocation_ids.serialize_ec2_query(
            value["allocation_ids"], pairs, f"{prefix}.AllocationIds"
        )
    if "attribute" in value:
        import aws_sdk_ec2.types.address_attribute_name

        aws_sdk_ec2.types.address_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeAddressesAttributeRequest:
    out: DescribeAddressesAttributeRequest = {}  # type: ignore[typeddict-item]
    if el.find("AllocationIds") is not None:
        import aws_sdk_ec2.types.allocation_ids

        out["allocation_ids"] = aws_sdk_ec2.types.allocation_ids.deserialize_ec2_query(
            el, "AllocationIds"
        )
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import aws_sdk_ec2.types.address_attribute_name

        out["attribute"] = (
            aws_sdk_ec2.types.address_attribute_name.deserialize_ec2_query(
                child_attribute
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
