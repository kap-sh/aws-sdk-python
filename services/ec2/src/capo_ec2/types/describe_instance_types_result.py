"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTypesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_type_info_list
    import capo_ec2.types.next_token


class DescribeInstanceTypesResult(TypedDict, closed=True):
    instance_types: NotRequired[
        "capo_ec2.types.instance_type_info_list.InstanceTypeInfoList"
    ]
    """<p>The instance type.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceTypesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_types" in value:
        import capo_ec2.types.instance_type_info_list

        capo_ec2.types.instance_type_info_list.serialize_ec2_query(
            value["instance_types"], pairs, f"{key_prefix}InstanceTypeSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceTypesResult:
    out: DescribeInstanceTypesResult = {}  # type: ignore[typeddict-item]
    child_instance_types = el.find("instanceTypeSet")
    if child_instance_types is not None:
        import capo_ec2.types.instance_type_info_list

        out["instance_types"] = (
            capo_ec2.types.instance_type_info_list.deserialize_ec2_query(
                child_instance_types
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
