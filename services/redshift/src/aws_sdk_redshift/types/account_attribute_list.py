"""Generated from Smithy shape ``com.amazonaws.redshift#AccountAttributeList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.attribute_list


class AccountAttributeList(TypedDict):
    account_attributes: NotRequired[
        "aws_sdk_redshift.types.attribute_list.AttributeList"
    ]
    """<p>A list of attributes assigned to an account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_attributes" in value:
        import aws_sdk_redshift.types.attribute_list

        aws_sdk_redshift.types.attribute_list.serialize_query(
            value["account_attributes"], pairs, f"{prefix}.AccountAttributes"
        )


def deserialize_query(el: Element) -> AccountAttributeList:
    out: AccountAttributeList = {}  # type: ignore[typeddict-item]
    child_account_attributes = el.find("AccountAttributes")
    if child_account_attributes is not None:
        import aws_sdk_redshift.types.attribute_list

        out["account_attributes"] = (
            aws_sdk_redshift.types.attribute_list.deserialize_query(
                child_account_attributes
            )
        )
    return out
