"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PublishSchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class PublishSchemaResponse(TypedDict):
    published_schema_arn: NotRequired["aws_sdk_clouddirectory.types.arn.Arn"]
    """<p>The ARN that is associated with the published schema. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishSchemaResponse) -> dict:
    out: dict = {}
    if "published_schema_arn" in value:
        out["PublishedSchemaArn"] = value["published_schema_arn"]
    return out


def deserialize_json(data: dict) -> PublishSchemaResponse:
    out: PublishSchemaResponse = {}  # type: ignore[typeddict-item]
    if "PublishedSchemaArn" in data:
        out["published_schema_arn"] = data["PublishedSchemaArn"]
    return out
