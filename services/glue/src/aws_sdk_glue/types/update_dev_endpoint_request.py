"""Generated from Smithy shape ``com.amazonaws.glue#UpdateDevEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean_value
    import aws_sdk_glue.types.dev_endpoint_custom_libraries
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.map_value
    import aws_sdk_glue.types.public_keys_list
    import aws_sdk_glue.types.string_list


class UpdateDevEndpointRequest(TypedDict):
    endpoint_name: "aws_sdk_glue.types.generic_string.GenericString"
    """<p>The name of the <code>DevEndpoint</code> to be updated.</p>"""
    public_key: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The public key for the <code>DevEndpoint</code> to use.</p>"""
    add_public_keys: NotRequired["aws_sdk_glue.types.public_keys_list.PublicKeysList"]
    """<p>The list of public keys for the <code>DevEndpoint</code> to use.</p>"""
    delete_public_keys: NotRequired[
        "aws_sdk_glue.types.public_keys_list.PublicKeysList"
    ]
    """<p>The list of public keys to be deleted from the <code>DevEndpoint</code>.</p>"""
    custom_libraries: NotRequired[
        "aws_sdk_glue.types.dev_endpoint_custom_libraries.DevEndpointCustomLibraries"
    ]
    """<p>Custom Python or Java libraries to be loaded in the <code>DevEndpoint</code>.</p>"""
    update_etl_libraries: "aws_sdk_glue.types.boolean_value.BooleanValue"
    """<p> <code>True</code> if the list of custom libraries to be loaded in the development endpoint needs to be updated, or <code>False</code> if otherwise.</p>"""
    delete_arguments: NotRequired["aws_sdk_glue.types.string_list.StringList"]
    """<p>The list of argument keys to be deleted from the map of arguments used to configure the <code>DevEndpoint</code>.</p>"""
    add_arguments: NotRequired["aws_sdk_glue.types.map_value.MapValue"]
    """<p>The map of arguments to add the map of arguments used to configure the <code>DevEndpoint</code>.</p> <p>Valid arguments are:</p> <ul> <li> <p> <code>\"--enable-glue-datacatalog\": \"\"</code> </p> </li> </ul> <p>You can specify a version of Python support for development endpoints by using the <code>Arguments</code> parameter in the <code>CreateDevEndpoint</code> or <code>UpdateDevEndpoint</code> APIs. If no arguments are provided, the version defaults to Python 2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDevEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointName"] = value["endpoint_name"]
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    if "add_public_keys" in value:
        import aws_sdk_glue.types.public_keys_list

        out["AddPublicKeys"] = (
            aws_sdk_glue.types.public_keys_list.serialize_aws_json_1_1(
                value["add_public_keys"]
            )
        )
    if "delete_public_keys" in value:
        import aws_sdk_glue.types.public_keys_list

        out["DeletePublicKeys"] = (
            aws_sdk_glue.types.public_keys_list.serialize_aws_json_1_1(
                value["delete_public_keys"]
            )
        )
    if "custom_libraries" in value:
        import aws_sdk_glue.types.dev_endpoint_custom_libraries

        out["CustomLibraries"] = (
            aws_sdk_glue.types.dev_endpoint_custom_libraries.serialize_aws_json_1_1(
                value["custom_libraries"]
            )
        )
    out["UpdateEtlLibraries"] = value.get("update_etl_libraries", False)
    if "delete_arguments" in value:
        import aws_sdk_glue.types.string_list

        out["DeleteArguments"] = aws_sdk_glue.types.string_list.serialize_aws_json_1_1(
            value["delete_arguments"]
        )
    if "add_arguments" in value:
        import aws_sdk_glue.types.map_value

        out["AddArguments"] = aws_sdk_glue.types.map_value.serialize_aws_json_1_1(
            value["add_arguments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDevEndpointRequest:
    out: UpdateDevEndpointRequest = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    else:
        raise DeserializationError("UpdateDevEndpointRequest.endpoint_name required")
    if "PublicKey" in data:
        out["public_key"] = data["PublicKey"]
    if "AddPublicKeys" in data:
        import aws_sdk_glue.types.public_keys_list

        out["add_public_keys"] = (
            aws_sdk_glue.types.public_keys_list.deserialize_aws_json_1_1(
                data["AddPublicKeys"]
            )
        )
    if "DeletePublicKeys" in data:
        import aws_sdk_glue.types.public_keys_list

        out["delete_public_keys"] = (
            aws_sdk_glue.types.public_keys_list.deserialize_aws_json_1_1(
                data["DeletePublicKeys"]
            )
        )
    if "CustomLibraries" in data:
        import aws_sdk_glue.types.dev_endpoint_custom_libraries

        out["custom_libraries"] = (
            aws_sdk_glue.types.dev_endpoint_custom_libraries.deserialize_aws_json_1_1(
                data["CustomLibraries"]
            )
        )
    if "UpdateEtlLibraries" in data:
        out["update_etl_libraries"] = data["UpdateEtlLibraries"]
    else:
        out["update_etl_libraries"] = False
    if "DeleteArguments" in data:
        import aws_sdk_glue.types.string_list

        out["delete_arguments"] = (
            aws_sdk_glue.types.string_list.deserialize_aws_json_1_1(
                data["DeleteArguments"]
            )
        )
    if "AddArguments" in data:
        import aws_sdk_glue.types.map_value

        out["add_arguments"] = aws_sdk_glue.types.map_value.deserialize_aws_json_1_1(
            data["AddArguments"]
        )
    return out
