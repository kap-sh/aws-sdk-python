"""Generated from Smithy shape ``com.amazonaws.personalize#CreateSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateSchemaResponse(TypedDict, closed=True):
    schema_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the created schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSchemaResponse) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["schemaArn"] = value["schema_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSchemaResponse:
    out: CreateSchemaResponse = {}  # type: ignore[typeddict-item]
    if "schemaArn" in data:
        out["schema_arn"] = data["schemaArn"]
    return out
