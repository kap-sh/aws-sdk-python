"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTypeOfferingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_type_offerings_list
    import capo_ec2.types.next_token


class DescribeInstanceTypeOfferingsResult(TypedDict, closed=True):
    instance_type_offerings: NotRequired[
        "capo_ec2.types.instance_type_offerings_list.InstanceTypeOfferingsList"
    ]
    """<p>The instance types offered in the location.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceTypeOfferingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_type_offerings" in value:
        import capo_ec2.types.instance_type_offerings_list

        capo_ec2.types.instance_type_offerings_list.serialize_ec2_query(
            value["instance_type_offerings"],
            pairs,
            f"{key_prefix}InstanceTypeOfferingSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceTypeOfferingsResult:
    out: DescribeInstanceTypeOfferingsResult = {}  # type: ignore[typeddict-item]
    if el.find("instanceTypeOfferingSet") is not None:
        import capo_ec2.types.instance_type_offerings_list

        out["instance_type_offerings"] = (
            capo_ec2.types.instance_type_offerings_list.deserialize_ec2_query(
                el, "instanceTypeOfferingSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
