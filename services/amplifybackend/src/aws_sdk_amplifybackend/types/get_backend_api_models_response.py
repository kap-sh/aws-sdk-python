"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetBackendAPIModelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.status


class GetBackendAPIModelsResponse(TypedDict):
    models: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Stringified JSON of the datastore model.</p>"""
    status: NotRequired["aws_sdk_amplifybackend.types.status.Status"]
    """<p>The current status of the request.</p>"""
    model_introspection_schema: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>Stringified JSON of the model introspection schema for an existing backend API resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendAPIModelsResponse) -> dict:
    out: dict = {}
    if "models" in value:
        out["models"] = value["models"]
    if "status" in value:
        import aws_sdk_amplifybackend.types.status

        out["status"] = aws_sdk_amplifybackend.types.status.serialize_json(
            value["status"]
        )
    if "model_introspection_schema" in value:
        out["modelIntrospectionSchema"] = value["model_introspection_schema"]
    return out


def deserialize_json(data: dict) -> GetBackendAPIModelsResponse:
    out: GetBackendAPIModelsResponse = {}  # type: ignore[typeddict-item]
    if "models" in data:
        out["models"] = data["models"]
    if "status" in data:
        import aws_sdk_amplifybackend.types.status

        out["status"] = aws_sdk_amplifybackend.types.status.deserialize_json(
            data["status"]
        )
    if "modelIntrospectionSchema" in data:
        out["model_introspection_schema"] = data["modelIntrospectionSchema"]
    return out
