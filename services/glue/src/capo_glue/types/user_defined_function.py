"""Generated from Smithy shape ``com.amazonaws.glue#UserDefinedFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.function_type
    import capo_glue.types.name_string
    import capo_glue.types.principal_type
    import capo_glue.types.resource_uri_list
    import capo_glue.types.timestamp


class UserDefinedFunction(TypedDict, closed=True):
    function_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the function.</p>"""
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the catalog database that contains the function.</p>"""
    class_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The Java class that contains the function code.</p>"""
    owner_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The owner of the function.</p>"""
    function_type: NotRequired["capo_glue.types.function_type.FunctionType"]
    """<p>The type of the function.</p>"""
    owner_type: NotRequired["capo_glue.types.principal_type.PrincipalType"]
    """<p>The owner type.</p>"""
    create_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the function was created.</p>"""
    resource_uris: NotRequired["capo_glue.types.resource_uri_list.ResourceUriList"]
    """<p>The resource URIs for the function.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the function resides.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDefinedFunction) -> dict:
    out: dict = {}
    if "function_name" in value:
        out["FunctionName"] = value["function_name"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "class_name" in value:
        out["ClassName"] = value["class_name"]
    if "owner_name" in value:
        out["OwnerName"] = value["owner_name"]
    if "function_type" in value:
        import capo_glue.types.function_type

        out["FunctionType"] = capo_glue.types.function_type.serialize_aws_json_1_1(
            value["function_type"]
        )
    if "owner_type" in value:
        import capo_glue.types.principal_type

        out["OwnerType"] = capo_glue.types.principal_type.serialize_aws_json_1_1(
            value["owner_type"]
        )
    if "create_time" in value:
        import capo_glue.types.timestamp

        out["CreateTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "resource_uris" in value:
        import capo_glue.types.resource_uri_list

        out["ResourceUris"] = capo_glue.types.resource_uri_list.serialize_aws_json_1_1(
            value["resource_uris"]
        )
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserDefinedFunction:
    out: UserDefinedFunction = {}  # type: ignore[typeddict-item]
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "ClassName" in data:
        out["class_name"] = data["ClassName"]
    if "OwnerName" in data:
        out["owner_name"] = data["OwnerName"]
    if "FunctionType" in data:
        import capo_glue.types.function_type

        out["function_type"] = capo_glue.types.function_type.deserialize_aws_json_1_1(
            data["FunctionType"]
        )
    if "OwnerType" in data:
        import capo_glue.types.principal_type

        out["owner_type"] = capo_glue.types.principal_type.deserialize_aws_json_1_1(
            data["OwnerType"]
        )
    if "CreateTime" in data:
        import capo_glue.types.timestamp

        out["create_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if "ResourceUris" in data:
        import capo_glue.types.resource_uri_list

        out["resource_uris"] = (
            capo_glue.types.resource_uri_list.deserialize_aws_json_1_1(
                data["ResourceUris"]
            )
        )
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    return out
