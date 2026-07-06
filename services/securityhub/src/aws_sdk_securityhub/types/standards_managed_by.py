"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsManagedBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class StandardsManagedBy(TypedDict, closed=True):
    company: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An identifier for the company that manages a specific security standard. For existing standards, the value is equal to <code>Amazon Web Services</code>.</p>"""
    product: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An identifier for the product that manages a specific security standard. For existing standards, the value is equal to the Amazon Web Services service that manages the standard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsManagedBy) -> dict:
    out: dict = {}
    if "company" in value:
        out["Company"] = value["company"]
    if "product" in value:
        out["Product"] = value["product"]
    return out


def deserialize_json(data: dict) -> StandardsManagedBy:
    out: StandardsManagedBy = {}  # type: ignore[typeddict-item]
    if "Company" in data:
        out["company"] = data["Company"]
    if "Product" in data:
        out["product"] = data["Product"]
    return out
