"""Generated from Smithy shape ``com.amazonaws.glue#UserDefinedFunctionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.function_type
    import capo_glue.types.name_string
    import capo_glue.types.principal_type
    import capo_glue.types.resource_uri_list


class UserDefinedFunctionInput(TypedDict, closed=True):
    function_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the function.</p>"""
    class_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The Java class that contains the function code.</p>"""
    owner_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The owner of the function.</p>"""
    function_type: NotRequired["capo_glue.types.function_type.FunctionType"]
    """<p>The type of the function.</p>"""
    owner_type: NotRequired["capo_glue.types.principal_type.PrincipalType"]
    """<p>The owner type.</p>"""
    resource_uris: NotRequired["capo_glue.types.resource_uri_list.ResourceUriList"]
    """<p>The resource URIs for the function.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDefinedFunctionInput) -> dict:
    out: dict = {}
    if "function_name" in value:
        out["FunctionName"] = value["function_name"]
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
    if "resource_uris" in value:
        import capo_glue.types.resource_uri_list

        out["ResourceUris"] = capo_glue.types.resource_uri_list.serialize_aws_json_1_1(
            value["resource_uris"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserDefinedFunctionInput:
    out: UserDefinedFunctionInput = {}  # type: ignore[typeddict-item]
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
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
    if "ResourceUris" in data:
        import capo_glue.types.resource_uri_list

        out["resource_uris"] = (
            capo_glue.types.resource_uri_list.deserialize_aws_json_1_1(
                data["ResourceUris"]
            )
        )
    return out
