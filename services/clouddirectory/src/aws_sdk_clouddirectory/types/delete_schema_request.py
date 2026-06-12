"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DeleteSchemaRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class DeleteSchemaRequest(TypedDict):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSchemaRequest:
    out: DeleteSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
