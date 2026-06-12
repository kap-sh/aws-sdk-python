"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#IntentMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.description
    import aws_sdk_lex_model_building_service.types.intent_name
    import aws_sdk_lex_model_building_service.types.timestamp
    import aws_sdk_lex_model_building_service.types.version


class IntentMetadata(TypedDict):
    name: NotRequired["aws_sdk_lex_model_building_service.types.intent_name.IntentName"]
    """<p>The name of the intent.</p>"""
    description: NotRequired[
        "aws_sdk_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the intent.</p>"""
    last_updated_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the intent was updated. When you create an intent, the creation date and last updated date are the same.</p>"""
    created_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the intent was created.</p>"""
    version: NotRequired["aws_sdk_lex_model_building_service.types.version.Version"]
    """<p>The version of the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "last_updated_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> IntentMetadata:
    out: IntentMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "lastUpdatedDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "createdDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["created_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    return out
