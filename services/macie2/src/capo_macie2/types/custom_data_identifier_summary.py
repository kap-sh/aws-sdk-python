"""Generated from Smithy shape ``com.amazonaws.macie2#CustomDataIdentifierSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.__timestamp_iso8601


class CustomDataIdentifierSummary(TypedDict, closed=True):
    arn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the custom data identifier.</p>"""
    created_at: NotRequired["capo_macie2.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created.</p>"""
    description: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The custom description of the custom data identifier.</p>"""
    id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the custom data identifier.</p>"""
    name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The custom name of the custom data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDataIdentifierSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["createdAt"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CustomDataIdentifierSummary:
    out: CustomDataIdentifierSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import capo_macie2.types.__timestamp_iso8601

        out["created_at"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
