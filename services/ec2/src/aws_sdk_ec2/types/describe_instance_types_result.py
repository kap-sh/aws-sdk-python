"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTypesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_info_list
    import aws_sdk_ec2.types.next_token


class DescribeInstanceTypesResult(TypedDict):
    instance_types: NotRequired[
        "aws_sdk_ec2.types.instance_type_info_list.InstanceTypeInfoList"
    ]
    """<p>The instance type.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceTypesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_types" in value:
        import aws_sdk_ec2.types.instance_type_info_list

        aws_sdk_ec2.types.instance_type_info_list.serialize_ec2_query(
            value["instance_types"], pairs, f"{prefix}.InstanceTypeSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceTypesResult:
    out: DescribeInstanceTypesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceTypeSet") is not None:
        import aws_sdk_ec2.types.instance_type_info_list

        out["instance_types"] = (
            aws_sdk_ec2.types.instance_type_info_list.deserialize_ec2_query(
                el, "InstanceTypeSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
