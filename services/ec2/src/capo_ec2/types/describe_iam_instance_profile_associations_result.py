"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIamInstanceProfileAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.iam_instance_profile_association_set
    import capo_ec2.types.next_token


class DescribeIamInstanceProfileAssociationsResult(TypedDict, closed=True):
    iam_instance_profile_associations: NotRequired[
        "capo_ec2.types.iam_instance_profile_association_set.IamInstanceProfileAssociationSet"
    ]
    """<p>Information about the IAM instance profile associations.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIamInstanceProfileAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "iam_instance_profile_associations" in value:
        import capo_ec2.types.iam_instance_profile_association_set

        capo_ec2.types.iam_instance_profile_association_set.serialize_ec2_query(
            value["iam_instance_profile_associations"],
            pairs,
            f"{key_prefix}IamInstanceProfileAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIamInstanceProfileAssociationsResult:
    out: DescribeIamInstanceProfileAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("iamInstanceProfileAssociationSet") is not None:
        import capo_ec2.types.iam_instance_profile_association_set

        out["iam_instance_profile_associations"] = (
            capo_ec2.types.iam_instance_profile_association_set.deserialize_ec2_query(
                el, "iamInstanceProfileAssociationSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
