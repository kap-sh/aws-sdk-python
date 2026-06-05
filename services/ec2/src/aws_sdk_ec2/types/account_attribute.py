"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_value_list
    import aws_sdk_ec2.types.string


class AccountAttribute(TypedDict):
    attribute_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the account attribute.</p>"""
    attribute_values: NotRequired[
        "aws_sdk_ec2.types.account_attribute_value_list.AccountAttributeValueList"
    ]
    """<p>The values for the account attribute.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute_name" in value:
        pairs.append((f"{prefix}.AttributeName", str(value["attribute_name"])))
    if "attribute_values" in value:
        import aws_sdk_ec2.types.account_attribute_value_list

        aws_sdk_ec2.types.account_attribute_value_list.serialize_ec2_query(
            value["attribute_values"], pairs, f"{prefix}.AttributeValueSet"
        )


def deserialize_ec2_query(el: Element) -> AccountAttribute:
    out: AccountAttribute = {}  # type: ignore[typeddict-item]
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    if el.find("AttributeValueSet") is not None:
        import aws_sdk_ec2.types.account_attribute_value_list

        out["attribute_values"] = (
            aws_sdk_ec2.types.account_attribute_value_list.deserialize_ec2_query(
                el, "AttributeValueSet"
            )
        )
    return out
