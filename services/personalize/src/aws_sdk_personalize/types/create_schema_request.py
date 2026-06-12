"""Generated from Smithy shape ``com.amazonaws.personalize#CreateSchemaRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.avro_schema
    import aws_sdk_personalize.types.domain
    import aws_sdk_personalize.types.name


class CreateSchemaRequest(TypedDict):
    name: "aws_sdk_personalize.types.name.Name"
    """<p>The name for the schema.</p>"""
    schema: "aws_sdk_personalize.types.avro_schema.AvroSchema"
    """<p>A schema in Avro JSON format.</p>"""
    domain: NotRequired["aws_sdk_personalize.types.domain.Domain"]
    """<p>The domain for the schema. If you are creating a schema for a dataset in a Domain dataset group, specify the domain you chose when you created the Domain dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSchemaRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["schema"] = value["schema"]
    if "domain" in value:
        import aws_sdk_personalize.types.domain

        out["domain"] = aws_sdk_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSchemaRequest:
    out: CreateSchemaRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSchemaRequest.name required")
    if "schema" in data:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("CreateSchemaRequest.schema required")
    if "domain" in data:
        import aws_sdk_personalize.types.domain

        out["domain"] = aws_sdk_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out
