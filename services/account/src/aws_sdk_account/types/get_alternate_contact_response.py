"""Generated from Smithy shape ``com.amazonaws.account#GetAlternateContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_account.types.alternate_contact


class GetAlternateContactResponse(TypedDict, closed=True):
    alternate_contact: NotRequired[
        "aws_sdk_account.types.alternate_contact.AlternateContact"
    ]
    """<p>A structure that contains the details for the specified alternate contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAlternateContactResponse) -> dict:
    out: dict = {}
    if "alternate_contact" in value:
        import aws_sdk_account.types.alternate_contact

        out["AlternateContact"] = (
            aws_sdk_account.types.alternate_contact.serialize_json(
                value["alternate_contact"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAlternateContactResponse:
    out: GetAlternateContactResponse = {}  # type: ignore[typeddict-item]
    if "AlternateContact" in data:
        import aws_sdk_account.types.alternate_contact

        out["alternate_contact"] = (
            aws_sdk_account.types.alternate_contact.deserialize_json(
                data["AlternateContact"]
            )
        )
    return out
