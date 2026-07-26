"""Generated from Smithy shape ``com.amazonaws.redshift#AccountAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.attribute_value_list
    import capo_redshift.types.string


class AccountAttribute(TypedDict, closed=True):
    attribute_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the attribute.</p>"""
    attribute_values: NotRequired[
        "capo_redshift.types.attribute_value_list.AttributeValueList"
    ]
    """<p>A list of attribute values.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute_name" in value:
        pairs.append((f"{prefix}.AttributeName", str(value["attribute_name"])))
    if "attribute_values" in value:
        import capo_redshift.types.attribute_value_list

        capo_redshift.types.attribute_value_list.serialize_query(
            value["attribute_values"], pairs, f"{prefix}.AttributeValues"
        )


def deserialize_query(el: Element) -> AccountAttribute:
    out: AccountAttribute = {}  # type: ignore[typeddict-item]
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    child_attribute_values = el.find("AttributeValues")
    if child_attribute_values is not None:
        import capo_redshift.types.attribute_value_list

        out["attribute_values"] = (
            capo_redshift.types.attribute_value_list.deserialize_query(
                child_attribute_values
            )
        )
    return out
