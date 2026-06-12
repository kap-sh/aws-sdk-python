"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetAppliedSchemaVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class GetAppliedSchemaVersionRequest(TypedDict):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the applied schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppliedSchemaVersionRequest) -> dict:
    out: dict = {}
    out["SchemaArn"] = value["schema_arn"]
    return out


def deserialize_json(data: dict) -> GetAppliedSchemaVersionRequest:
    out: GetAppliedSchemaVersionRequest = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    else:
        raise DeserializationError("GetAppliedSchemaVersionRequest.schema_arn required")
    return out
