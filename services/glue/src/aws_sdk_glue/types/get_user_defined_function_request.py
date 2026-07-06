"""Generated from Smithy shape ``com.amazonaws.glue#GetUserDefinedFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string


class GetUserDefinedFunctionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the function to be retrieved is located. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the function is located.</p>"""
    function_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the function.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserDefinedFunctionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["FunctionName"] = value["function_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserDefinedFunctionRequest:
    out: GetUserDefinedFunctionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "GetUserDefinedFunctionRequest.database_name required"
        )
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError(
            "GetUserDefinedFunctionRequest.function_name required"
        )
    return out
