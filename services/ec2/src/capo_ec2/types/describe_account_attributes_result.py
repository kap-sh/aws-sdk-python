"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAccountAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_attribute_list


class DescribeAccountAttributesResult(TypedDict, closed=True):
    account_attributes: NotRequired[
        "capo_ec2.types.account_attribute_list.AccountAttributeList"
    ]
    """<p>Information about the account attributes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAccountAttributesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "account_attributes" in value:
        import capo_ec2.types.account_attribute_list

        capo_ec2.types.account_attribute_list.serialize_ec2_query(
            value["account_attributes"], pairs, f"{key_prefix}AccountAttributeSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeAccountAttributesResult:
    out: DescribeAccountAttributesResult = {}  # type: ignore[typeddict-item]
    child_account_attributes = el.find("accountAttributeSet")
    if child_account_attributes is not None:
        import capo_ec2.types.account_attribute_list

        out["account_attributes"] = (
            capo_ec2.types.account_attribute_list.deserialize_ec2_query(
                child_account_attributes
            )
        )
    return out
