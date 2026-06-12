"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PutSchemaFromJsonRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.schema_json_document


class PutSchemaFromJsonRequest(TypedDict):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the schema to update.</p>"""
    document: "aws_sdk_clouddirectory.types.schema_json_document.SchemaJsonDocument"
    """<p>The replacement JSON schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSchemaFromJsonRequest) -> dict:
    out: dict = {}
    out["Document"] = value["document"]
    return out


def deserialize_json(data: dict) -> PutSchemaFromJsonRequest:
    out: PutSchemaFromJsonRequest = {}  # type: ignore[typeddict-item]
    if "Document" in data:
        out["document"] = data["Document"]
    else:
        raise DeserializationError("PutSchemaFromJsonRequest.document required")
    return out
