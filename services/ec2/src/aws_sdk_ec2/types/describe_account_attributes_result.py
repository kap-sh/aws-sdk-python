"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAccountAttributesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_list


class DescribeAccountAttributesResult(TypedDict):
    account_attributes: NotRequired[
        "aws_sdk_ec2.types.account_attribute_list.AccountAttributeList"
    ]
    """<p>Information about the account attributes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAccountAttributesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_attributes" in value:
        import aws_sdk_ec2.types.account_attribute_list

        aws_sdk_ec2.types.account_attribute_list.serialize_ec2_query(
            value["account_attributes"], pairs, f"{prefix}.AccountAttributeSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeAccountAttributesResult:
    out: DescribeAccountAttributesResult = {}  # type: ignore[typeddict-item]
    if el.find("AccountAttributeSet") is not None:
        import aws_sdk_ec2.types.account_attribute_list

        out["account_attributes"] = (
            aws_sdk_ec2.types.account_attribute_list.deserialize_ec2_query(
                el, "AccountAttributeSet"
            )
        )
    return out
