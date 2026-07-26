"""Generated from Smithy shape ``com.amazonaws.macie2#ManagedDataIdentifierSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.sensitive_data_item_category


class ManagedDataIdentifierSummary(TypedDict, closed=True):
    category: NotRequired[
        "capo_macie2.types.sensitive_data_item_category.SensitiveDataItemCategory"
    ]
    """<p>The category of sensitive data that the managed data identifier detects: CREDENTIALS, for credentials data such as private keys or Amazon Web Services secret access keys; FINANCIAL_INFORMATION, for financial data such as credit card numbers; or, PERSONAL_INFORMATION, for personal health information, such as health insurance identification numbers, or personally identifiable information, such as passport numbers.</p>"""
    id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the managed data identifier. This is a string that describes the type of sensitive data that the managed data identifier detects. For example: OPENSSH_PRIVATE_KEY for OpenSSH private keys, CREDIT_CARD_NUMBER for credit card numbers, or USA_PASSPORT_NUMBER for US passport numbers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedDataIdentifierSummary) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_macie2.types.sensitive_data_item_category

        out["category"] = capo_macie2.types.sensitive_data_item_category.serialize_json(
            value["category"]
        )
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ManagedDataIdentifierSummary:
    out: ManagedDataIdentifierSummary = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import capo_macie2.types.sensitive_data_item_category

        out["category"] = (
            capo_macie2.types.sensitive_data_item_category.deserialize_json(
                data["category"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    return out
