"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceCreditSpecificationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_credit_specification_list
    import capo_ec2.types.string


class DescribeInstanceCreditSpecificationsResult(TypedDict, closed=True):
    instance_credit_specifications: NotRequired[
        "capo_ec2.types.instance_credit_specification_list.InstanceCreditSpecificationList"
    ]
    """<p>Information about the credit option for CPU usage of an instance.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceCreditSpecificationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_credit_specifications" in value:
        import capo_ec2.types.instance_credit_specification_list

        capo_ec2.types.instance_credit_specification_list.serialize_ec2_query(
            value["instance_credit_specifications"],
            pairs,
            f"{prefix}.InstanceCreditSpecificationSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceCreditSpecificationsResult:
    out: DescribeInstanceCreditSpecificationsResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceCreditSpecificationSet") is not None:
        import capo_ec2.types.instance_credit_specification_list

        out["instance_credit_specifications"] = (
            capo_ec2.types.instance_credit_specification_list.deserialize_ec2_query(
                el, "InstanceCreditSpecificationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
