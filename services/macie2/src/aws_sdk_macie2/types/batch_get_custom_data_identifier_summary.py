"""Generated from Smithy shape ``com.amazonaws.macie2#BatchGetCustomDataIdentifierSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601


class BatchGetCustomDataIdentifierSummary(TypedDict):
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the custom data identifier.</p>"""
    created_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created.</p>"""
    deleted: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the custom data identifier was deleted. If you delete a custom data identifier, Amazon Macie doesn't delete it permanently. Instead, it soft deletes the identifier.</p>"""
    description: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The custom description of the custom data identifier.</p>"""
    id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the custom data identifier.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The custom name of the custom data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCustomDataIdentifierSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["createdAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "deleted" in value:
        out["deleted"] = value["deleted"]
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> BatchGetCustomDataIdentifierSummary:
    out: BatchGetCustomDataIdentifierSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["created_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "deleted" in data:
        out["deleted"] = data["deleted"]
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
