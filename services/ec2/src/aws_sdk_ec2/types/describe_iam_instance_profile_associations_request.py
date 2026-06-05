"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIamInstanceProfileAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.association_id_list
    import aws_sdk_ec2.types.describe_iam_instance_profile_associations_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token


class DescribeIamInstanceProfileAssociationsRequest(TypedDict):
    association_ids: NotRequired[
        "aws_sdk_ec2.types.association_id_list.AssociationIdList"
    ]
    """<p>The IAM instance profile associations.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>instance-id</code> - The ID of the instance.</p> </li> <li> <p> <code>state</code> - The state of the association (<code>associating</code> | <code>associated</code> | <code>disassociating</code>).</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_iam_instance_profile_associations_max_results.DescribeIamInstanceProfileAssociationsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIamInstanceProfileAssociationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association_ids" in value:
        import aws_sdk_ec2.types.association_id_list

        aws_sdk_ec2.types.association_id_list.serialize_ec2_query(
            value["association_ids"], pairs, f"{prefix}.AssociationIds"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIamInstanceProfileAssociationsRequest:
    out: DescribeIamInstanceProfileAssociationsRequest = {}  # type: ignore[typeddict-item]
    if el.find("AssociationIds") is not None:
        import aws_sdk_ec2.types.association_id_list

        out["association_ids"] = (
            aws_sdk_ec2.types.association_id_list.deserialize_ec2_query(
                el, "AssociationIds"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
