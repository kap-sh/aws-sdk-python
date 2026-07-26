"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.avro_schema
    import capo_personalize.types.date
    import capo_personalize.types.domain
    import capo_personalize.types.name


class DatasetSchema(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the schema.</p>"""
    schema_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the schema.</p>"""
    schema: NotRequired["capo_personalize.types.avro_schema.AvroSchema"]
    """<p>The schema.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the schema was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the schema was last updated.</p>"""
    domain: NotRequired["capo_personalize.types.domain.Domain"]
    """<p>The domain of a schema that you created for a dataset in a Domain dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetSchema) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "schema_arn" in value:
        out["schemaArn"] = value["schema_arn"]
    if "schema" in value:
        out["schema"] = value["schema"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "domain" in value:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetSchema:
    out: DatasetSchema = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "schemaArn" in data:
        out["schema_arn"] = data["schemaArn"]
    if "schema" in data:
        out["schema"] = data["schema"]
    if "creationDateTime" in data:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "domain" in data:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out
