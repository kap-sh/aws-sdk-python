"""Generated from Smithy shape ``com.amazonaws.glue#GetPartitionIndexesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.token


class GetPartitionIndexesRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID where the table resides.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Specifies the name of a database from which you want to retrieve partition indexes.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Specifies the name of a table for which you want to retrieve the partition indexes.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, included if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPartitionIndexesRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPartitionIndexesRequest:
    out: GetPartitionIndexesRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetPartitionIndexesRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetPartitionIndexesRequest.table_name required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
