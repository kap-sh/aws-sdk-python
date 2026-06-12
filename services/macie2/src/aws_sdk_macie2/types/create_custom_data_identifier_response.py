"""Generated from Smithy shape ``com.amazonaws.macie2#CreateCustomDataIdentifierResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class CreateCustomDataIdentifierResponse(TypedDict):
    custom_data_identifier_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the custom data identifier that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomDataIdentifierResponse) -> dict:
    out: dict = {}
    if "custom_data_identifier_id" in value:
        out["customDataIdentifierId"] = value["custom_data_identifier_id"]
    return out


def deserialize_json(data: dict) -> CreateCustomDataIdentifierResponse:
    out: CreateCustomDataIdentifierResponse = {}  # type: ignore[typeddict-item]
    if "customDataIdentifierId" in data:
        out["custom_data_identifier_id"] = data["customDataIdentifierId"]
    return out
