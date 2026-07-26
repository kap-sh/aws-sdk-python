"""Generated from Smithy shape ``com.amazonaws.firehose#SchemaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.non_empty_string_without_whitespace


class SchemaConfiguration(TypedDict, closed=True):
    role_arn: NotRequired[
        "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    ]
    """<p>The role that Firehose can use to access Amazon Web Services Glue. This role must be in the same account you use for Firehose. Cross-account roles aren't allowed.</p> <important> <p>If the <code>SchemaConfiguration</code> request parameter is used as part of invoking the <code>CreateDeliveryStream</code> API, then the <code>RoleARN</code> property is required and its value must be specified.</p> </important>"""
    catalog_id: NotRequired[
        "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    ]
    """<p>The ID of the Amazon Web Services Glue Data Catalog. If you don't supply this, the Amazon Web Services account ID is used by default.</p>"""
    database_name: NotRequired[
        "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    ]
    """<p>Specifies the name of the Amazon Web Services Glue database that contains the schema for the output data.</p> <important> <p>If the <code>SchemaConfiguration</code> request parameter is used as part of invoking the <code>CreateDeliveryStream</code> API, then the <code>DatabaseName</code> property is required and its value must be specified.</p> </important>"""
    table_name: NotRequired[
        "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    ]
    """<p>Specifies the Amazon Web Services Glue table that contains the column information that constitutes your data schema.</p> <important> <p>If the <code>SchemaConfiguration</code> request parameter is used as part of invoking the <code>CreateDeliveryStream</code> API, then the <code>TableName</code> property is required and its value must be specified.</p> </important>"""
    region: NotRequired[
        "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    ]
    """<p>If you don't specify an Amazon Web Services Region, the default is the current Region.</p>"""
    version_id: NotRequired[
        "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    ]
    """<p>Specifies the table version for the output data schema. If you don't specify this version ID, or if you set it to <code>LATEST</code>, Firehose uses the most recent version. This means that any updates to the table are automatically picked up.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaConfiguration) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "region" in value:
        out["Region"] = value["region"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaConfiguration:
    out: SchemaConfiguration = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
