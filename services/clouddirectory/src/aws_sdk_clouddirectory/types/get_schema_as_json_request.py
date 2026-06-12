"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetSchemaAsJsonRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class GetSchemaAsJsonRequest(TypedDict):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the schema to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaAsJsonRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSchemaAsJsonRequest:
    out: GetSchemaAsJsonRequest = {}  # type: ignore[typeddict-item]
    return out
