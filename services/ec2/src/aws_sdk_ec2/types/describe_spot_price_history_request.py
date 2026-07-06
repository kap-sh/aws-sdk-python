"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotPriceHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_type_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.product_description_list
    import aws_sdk_ec2.types.string


class DescribeSpotPriceHistoryRequest(TypedDict, closed=True):
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>Filters the results by the specified ID of the Availability Zone.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time, up to the past 90 days, from which to start retrieving the price history data, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    end_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time, up to the current date, from which to stop retrieving the price history data, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    instance_types: NotRequired["aws_sdk_ec2.types.instance_type_list.InstanceTypeList"]
    """<p>Filters the results by the specified instance types.</p>"""
    product_descriptions: NotRequired[
        "aws_sdk_ec2.types.product_description_list.ProductDescriptionList"
    ]
    """<p>Filters the results by the specified basic product descriptions.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone for which prices should be returned.</p> </li> <li> <p> <code>availability-zone-id</code> - The ID of the Availability Zone for which prices should be returned.</p> </li> <li> <p> <code>instance-type</code> - The type of instance (for example, <code>m3.medium</code>).</p> </li> <li> <p> <code>product-description</code> - The product description for the Spot price (<code>Linux/UNIX</code> | <code>Red Hat Enterprise Linux</code> | <code>SUSE Linux</code> | <code>Windows</code> | <code>Linux/UNIX (Amazon VPC)</code> | <code>Red Hat Enterprise Linux (Amazon VPC)</code> | <code>SUSE Linux (Amazon VPC)</code> | <code>Windows (Amazon VPC)</code>).</p> </li> <li> <p> <code>spot-price</code> - The Spot price. The value must match exactly (or use wildcards; greater than or less than comparison is not supported).</p> </li> <li> <p> <code>timestamp</code> - The time stamp of the Spot price history, in UTC format (for example, <i>ddd MMM dd HH</i>:<i>mm</i>:<i>ss</i> UTC <i>YYYY</i>). You can use wildcards (<code>*</code> and <code>?</code>). Greater than or less than comparison is not supported.</p> </li> </ul>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Filters the results by the specified Availability Zone.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotPriceHistoryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "start_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "instance_types" in value:
        import aws_sdk_ec2.types.instance_type_list

        aws_sdk_ec2.types.instance_type_list.serialize_ec2_query(
            value["instance_types"], pairs, f"{prefix}.InstanceTypes"
        )
    if "product_descriptions" in value:
        import aws_sdk_ec2.types.product_description_list

        aws_sdk_ec2.types.product_description_list.serialize_ec2_query(
            value["product_descriptions"], pairs, f"{prefix}.ProductDescriptions"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSpotPriceHistoryRequest:
    out: DescribeSpotPriceHistoryRequest = {}  # type: ignore[typeddict-item]
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_ec2.types.date_time

        out["start_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import aws_sdk_ec2.types.date_time

        out["end_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_end_time
        )
    if el.find("InstanceTypes") is not None:
        import aws_sdk_ec2.types.instance_type_list

        out["instance_types"] = (
            aws_sdk_ec2.types.instance_type_list.deserialize_ec2_query(
                el, "InstanceTypes"
            )
        )
    if el.find("ProductDescriptions") is not None:
        import aws_sdk_ec2.types.product_description_list

        out["product_descriptions"] = (
            aws_sdk_ec2.types.product_description_list.deserialize_ec2_query(
                el, "ProductDescriptions"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
