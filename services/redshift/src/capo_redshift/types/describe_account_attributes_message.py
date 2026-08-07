"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeAccountAttributesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.attribute_name_list


class DescribeAccountAttributesMessage(TypedDict, closed=True):
    attribute_names: NotRequired[
        "capo_redshift.types.attribute_name_list.AttributeNameList"
    ]
    """<p>A list of attribute names.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountAttributesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute_names" in value:
        import capo_redshift.types.attribute_name_list

        capo_redshift.types.attribute_name_list.serialize_query(
            value["attribute_names"], pairs, f"{key_prefix}AttributeNames"
        )


def deserialize_query(el: Element) -> DescribeAccountAttributesMessage:
    out: DescribeAccountAttributesMessage = {}  # type: ignore[typeddict-item]
    child_attribute_names = el.find("AttributeNames")
    if child_attribute_names is not None:
        import capo_redshift.types.attribute_name_list

        out["attribute_names"] = (
            capo_redshift.types.attribute_name_list.deserialize_query(
                child_attribute_names
            )
        )
    return out
