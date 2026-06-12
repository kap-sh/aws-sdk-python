"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.generation_status
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.timestamp


class GenerationSummary(TypedDict):
    generation_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the generation request.</p>"""
    generation_status: NotRequired[
        "aws_sdk_lex_models_v2.types.generation_status.GenerationStatus"
    ]
    """<p>The status of the generation request.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time at which the generation request was made.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time at which the generation request was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationSummary) -> dict:
    out: dict = {}
    if "generation_id" in value:
        out["generationId"] = value["generation_id"]
    if "generation_status" in value:
        import aws_sdk_lex_models_v2.types.generation_status

        out["generationStatus"] = (
            aws_sdk_lex_models_v2.types.generation_status.serialize_json(
                value["generation_status"]
            )
        )
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerationSummary:
    out: GenerationSummary = {}  # type: ignore[typeddict-item]
    if "generationId" in data:
        out["generation_id"] = data["generationId"]
    if "generationStatus" in data:
        import aws_sdk_lex_models_v2.types.generation_status

        out["generation_status"] = (
            aws_sdk_lex_models_v2.types.generation_status.deserialize_json(
                data["generationStatus"]
            )
        )
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
