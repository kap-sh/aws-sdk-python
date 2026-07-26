"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.next_token
    import capo_ec2.types.verified_access_instance_list


class DescribeVerifiedAccessInstancesResult(TypedDict, closed=True):
    verified_access_instances: NotRequired[
        "capo_ec2.types.verified_access_instance_list.VerifiedAccessInstanceList"
    ]
    """<p>Details about the Verified Access instances.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVerifiedAccessInstancesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_instances" in value:
        import capo_ec2.types.verified_access_instance_list

        capo_ec2.types.verified_access_instance_list.serialize_ec2_query(
            value["verified_access_instances"],
            pairs,
            f"{prefix}.VerifiedAccessInstanceSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVerifiedAccessInstancesResult:
    out: DescribeVerifiedAccessInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("VerifiedAccessInstanceSet") is not None:
        import capo_ec2.types.verified_access_instance_list

        out["verified_access_instances"] = (
            capo_ec2.types.verified_access_instance_list.deserialize_ec2_query(
                el, "VerifiedAccessInstanceSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
