"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_attribute_value_list
    import capo_ec2.types.string


class AccountAttribute(TypedDict, closed=True):
    attribute_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the account attribute.</p>"""
    attribute_values: NotRequired[
        "capo_ec2.types.account_attribute_value_list.AccountAttributeValueList"
    ]
    """<p>The values for the account attribute.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute_name" in value:
        pairs.append((f"{key_prefix}AttributeName", str(value["attribute_name"])))
    if "attribute_values" in value:
        import capo_ec2.types.account_attribute_value_list

        capo_ec2.types.account_attribute_value_list.serialize_ec2_query(
            value["attribute_values"], pairs, f"{key_prefix}AttributeValueSet"
        )


def deserialize_ec2_query(el: Element) -> AccountAttribute:
    out: AccountAttribute = {}  # type: ignore[typeddict-item]
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    if el.find("AttributeValueSet") is not None:
        import capo_ec2.types.account_attribute_value_list

        out["attribute_values"] = (
            capo_ec2.types.account_attribute_value_list.deserialize_ec2_query(
                el, "AttributeValueSet"
            )
        )
    return out
