"""Generated from Smithy shape ``com.amazonaws.macie2#SuppressDataIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.data_identifier_type


class SuppressDataIdentifier(TypedDict, closed=True):
    id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the custom data identifier or managed data identifier that detected the type of sensitive data to exclude from the score.</p>"""
    type: NotRequired["aws_sdk_macie2.types.data_identifier_type.DataIdentifierType"]
    """<p>The type of data identifier that detected the sensitive data. Possible values are: CUSTOM, for a custom data identifier; and, MANAGED, for a managed data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressDataIdentifier) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import aws_sdk_macie2.types.data_identifier_type

        out["type"] = aws_sdk_macie2.types.data_identifier_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> SuppressDataIdentifier:
    out: SuppressDataIdentifier = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import aws_sdk_macie2.types.data_identifier_type

        out["type"] = aws_sdk_macie2.types.data_identifier_type.deserialize_json(
            data["type"]
        )
    return out
