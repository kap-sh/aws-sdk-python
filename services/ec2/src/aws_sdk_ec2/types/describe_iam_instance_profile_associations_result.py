"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIamInstanceProfileAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.iam_instance_profile_association_set
    import aws_sdk_ec2.types.next_token


class DescribeIamInstanceProfileAssociationsResult(TypedDict, closed=True):
    iam_instance_profile_associations: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_association_set.IamInstanceProfileAssociationSet"
    ]
    """<p>Information about the IAM instance profile associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIamInstanceProfileAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "iam_instance_profile_associations" in value:
        import aws_sdk_ec2.types.iam_instance_profile_association_set

        aws_sdk_ec2.types.iam_instance_profile_association_set.serialize_ec2_query(
            value["iam_instance_profile_associations"],
            pairs,
            f"{prefix}.IamInstanceProfileAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIamInstanceProfileAssociationsResult:
    out: DescribeIamInstanceProfileAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("IamInstanceProfileAssociationSet") is not None:
        import aws_sdk_ec2.types.iam_instance_profile_association_set

        out["iam_instance_profile_associations"] = (
            aws_sdk_ec2.types.iam_instance_profile_association_set.deserialize_ec2_query(
                el, "IamInstanceProfileAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
