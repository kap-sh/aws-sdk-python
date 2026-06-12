"""Generated from Smithy shape ``com.amazonaws.glue#CreateUserDefinedFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.user_defined_function_input


class CreateUserDefinedFunctionRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which to create the function. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which to create the function.</p>"""
    function_input: (
        "aws_sdk_glue.types.user_defined_function_input.UserDefinedFunctionInput"
    )
    """<p>A <code>FunctionInput</code> object that defines the function to create in the Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserDefinedFunctionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    import aws_sdk_glue.types.user_defined_function_input

    out["FunctionInput"] = (
        aws_sdk_glue.types.user_defined_function_input.serialize_aws_json_1_1(
            value["function_input"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserDefinedFunctionRequest:
    out: CreateUserDefinedFunctionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "CreateUserDefinedFunctionRequest.database_name required"
        )
    if "FunctionInput" in data:
        import aws_sdk_glue.types.user_defined_function_input

        out["function_input"] = (
            aws_sdk_glue.types.user_defined_function_input.deserialize_aws_json_1_1(
                data["FunctionInput"]
            )
        )
    else:
        raise DeserializationError(
            "CreateUserDefinedFunctionRequest.function_input required"
        )
    return out
