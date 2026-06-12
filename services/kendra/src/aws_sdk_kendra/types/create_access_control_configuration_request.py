"""Generated from Smithy shape ``com.amazonaws.kendra#CreateAccessControlConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.access_control_configuration_name
    import aws_sdk_kendra.types.client_token_name
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.hierarchical_principal_list
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.principal_list


class CreateAccessControlConfigurationRequest(TypedDict):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index to create an access control configuration for your documents.</p>"""
    name: "aws_sdk_kendra.types.access_control_configuration_name.AccessControlConfigurationName"
    """<p>A name for the access control configuration.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A description for the access control configuration.</p>"""
    access_control_list: NotRequired[
        "aws_sdk_kendra.types.principal_list.PrincipalList"
    ]
    """<p>Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>"""
    hierarchical_access_control_list: NotRequired[
        "aws_sdk_kendra.types.hierarchical_principal_list.HierarchicalPrincipalList"
    ]
    """<p>The list of <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html\">principal</a> lists that define the hierarchy for which documents users should have access to.</p>"""
    client_token: NotRequired["aws_sdk_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create an access control configuration. Multiple calls to the <code>CreateAccessControlConfiguration</code> API with the same client token will create only one access control configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccessControlConfigurationRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "access_control_list" in value:
        import aws_sdk_kendra.types.principal_list

        out["AccessControlList"] = (
            aws_sdk_kendra.types.principal_list.serialize_aws_json_1_1(
                value["access_control_list"]
            )
        )
    if "hierarchical_access_control_list" in value:
        import aws_sdk_kendra.types.hierarchical_principal_list

        out["HierarchicalAccessControlList"] = (
            aws_sdk_kendra.types.hierarchical_principal_list.serialize_aws_json_1_1(
                value["hierarchical_access_control_list"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccessControlConfigurationRequest:
    out: CreateAccessControlConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "CreateAccessControlConfigurationRequest.index_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "CreateAccessControlConfigurationRequest.name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "AccessControlList" in data:
        import aws_sdk_kendra.types.principal_list

        out["access_control_list"] = (
            aws_sdk_kendra.types.principal_list.deserialize_aws_json_1_1(
                data["AccessControlList"]
            )
        )
    if "HierarchicalAccessControlList" in data:
        import aws_sdk_kendra.types.hierarchical_principal_list

        out["hierarchical_access_control_list"] = (
            aws_sdk_kendra.types.hierarchical_principal_list.deserialize_aws_json_1_1(
                data["HierarchicalAccessControlList"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
