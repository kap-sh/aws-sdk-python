"""Generated from Smithy shape ``com.amazonaws.appsync#StartSchemaCreationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.blob
    import aws_sdk_appsync.types.string


class StartSchemaCreationRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    definition: "aws_sdk_appsync.types.blob.Blob"
    """<p>The schema definition, in GraphQL schema language format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSchemaCreationRequest) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.blob

    out["definition"] = aws_sdk_appsync.types.blob.serialize_json(value["definition"])
    return out


def deserialize_json(data: dict) -> StartSchemaCreationRequest:
    out: StartSchemaCreationRequest = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        import aws_sdk_appsync.types.blob

        out["definition"] = aws_sdk_appsync.types.blob.deserialize_json(
            data["definition"]
        )
    else:
        raise DeserializationError("StartSchemaCreationRequest.definition required")
    return out
