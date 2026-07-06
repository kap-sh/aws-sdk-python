"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceCreditSpecificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_instance_credit_specifications_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_id_string_list
    import aws_sdk_ec2.types.string


class DescribeInstanceCreditSpecificationsRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>instance-id</code> - The ID of the instance.</p> </li> </ul>"""
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The instance IDs.</p> <p>Default: Describes all your instances.</p> <p>Constraints: Maximum 1000 explicitly specified instance IDs.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_instance_credit_specifications_max_results.DescribeInstanceCreditSpecificationsMaxResults"
    ]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p> <p>You cannot specify this parameter and the instance IDs parameter in the same call.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceCreditSpecificationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "instance_ids" in value:
        import aws_sdk_ec2.types.instance_id_string_list

        aws_sdk_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceCreditSpecificationsRequest:
    out: DescribeInstanceCreditSpecificationsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    if el.find("InstanceIds") is not None:
        import aws_sdk_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            aws_sdk_ec2.types.instance_id_string_list.deserialize_ec2_query(
                el, "InstanceIds"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
