"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateAccessControlConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.access_control_configuration_id
    import aws_sdk_kendra.types.access_control_configuration_name
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.hierarchical_principal_list
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.principal_list


class UpdateAccessControlConfigurationRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for an access control configuration.</p>"""
    id: "aws_sdk_kendra.types.access_control_configuration_id.AccessControlConfigurationId"
    """<p>The identifier of the access control configuration you want to update.</p>"""
    name: NotRequired[
        "aws_sdk_kendra.types.access_control_configuration_name.AccessControlConfigurationName"
    ]
    """<p>A new name for the access control configuration.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A new description for the access control configuration.</p>"""
    access_control_list: NotRequired[
        "aws_sdk_kendra.types.principal_list.PrincipalList"
    ]
    """<p>Information you want to update on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>"""
    hierarchical_access_control_list: NotRequired[
        "aws_sdk_kendra.types.hierarchical_principal_list.HierarchicalPrincipalList"
    ]
    r"""<p>The updated list of <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html\">principal</a> lists that define the hierarchy for which documents users should have access to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAccessControlConfigurationRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Id"] = value["id"]
    if "name" in value:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAccessControlConfigurationRequest:
    out: UpdateAccessControlConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "UpdateAccessControlConfigurationRequest.index_id required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "UpdateAccessControlConfigurationRequest.id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
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
    return out
