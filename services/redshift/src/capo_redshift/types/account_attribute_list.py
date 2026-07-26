"""Generated from Smithy shape ``com.amazonaws.redshift#AccountAttributeList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.attribute_list


class AccountAttributeList(TypedDict, closed=True):
    account_attributes: NotRequired["capo_redshift.types.attribute_list.AttributeList"]
    """<p>A list of attributes assigned to an account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_attributes" in value:
        import capo_redshift.types.attribute_list

        capo_redshift.types.attribute_list.serialize_query(
            value["account_attributes"], pairs, f"{prefix}.AccountAttributes"
        )


def deserialize_query(el: Element) -> AccountAttributeList:
    out: AccountAttributeList = {}  # type: ignore[typeddict-item]
    child_account_attributes = el.find("AccountAttributes")
    if child_account_attributes is not None:
        import capo_redshift.types.attribute_list

        out["account_attributes"] = (
            capo_redshift.types.attribute_list.deserialize_query(
                child_account_attributes
            )
        )
    return out
