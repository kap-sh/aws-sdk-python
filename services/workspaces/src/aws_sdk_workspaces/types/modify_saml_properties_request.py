"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifySamlPropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.deletable_saml_properties_list
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.saml_properties


class ModifySamlPropertiesRequest(TypedDict):
    resource_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier for which you want to configure SAML properties.</p>"""
    saml_properties: NotRequired[
        "aws_sdk_workspaces.types.saml_properties.SamlProperties"
    ]
    """<p>The properties for configuring SAML 2.0 authentication.</p>"""
    properties_to_delete: NotRequired[
        "aws_sdk_workspaces.types.deletable_saml_properties_list.DeletableSamlPropertiesList"
    ]
    """<p>The SAML properties to delete as part of your request.</p> <p>Specify one of the following options:</p> <ul> <li> <p> <code>SAML_PROPERTIES_USER_ACCESS_URL</code> to delete the user access URL.</p> </li> <li> <p> <code>SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME</code> to delete the relay state parameter name.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifySamlPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "saml_properties" in value:
        import aws_sdk_workspaces.types.saml_properties

        out["SamlProperties"] = (
            aws_sdk_workspaces.types.saml_properties.serialize_aws_json_1_1(
                value["saml_properties"]
            )
        )
    if "properties_to_delete" in value:
        import aws_sdk_workspaces.types.deletable_saml_properties_list

        out["PropertiesToDelete"] = (
            aws_sdk_workspaces.types.deletable_saml_properties_list.serialize_aws_json_1_1(
                value["properties_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifySamlPropertiesRequest:
    out: ModifySamlPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ModifySamlPropertiesRequest.resource_id required")
    if "SamlProperties" in data:
        import aws_sdk_workspaces.types.saml_properties

        out["saml_properties"] = (
            aws_sdk_workspaces.types.saml_properties.deserialize_aws_json_1_1(
                data["SamlProperties"]
            )
        )
    if "PropertiesToDelete" in data:
        import aws_sdk_workspaces.types.deletable_saml_properties_list

        out["properties_to_delete"] = (
            aws_sdk_workspaces.types.deletable_saml_properties_list.deserialize_aws_json_1_1(
                data["PropertiesToDelete"]
            )
        )
    return out
