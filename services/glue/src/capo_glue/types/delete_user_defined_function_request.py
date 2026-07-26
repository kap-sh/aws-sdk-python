"""Generated from Smithy shape ``com.amazonaws.glue#DeleteUserDefinedFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string


class DeleteUserDefinedFunctionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the function to be deleted is located. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the function is located.</p>"""
    function_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the function definition to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserDefinedFunctionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["FunctionName"] = value["function_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserDefinedFunctionRequest:
    out: DeleteUserDefinedFunctionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "DeleteUserDefinedFunctionRequest.database_name required"
        )
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError(
            "DeleteUserDefinedFunctionRequest.function_name required"
        )
    return out
