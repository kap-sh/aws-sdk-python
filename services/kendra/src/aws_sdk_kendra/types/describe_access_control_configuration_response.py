"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeAccessControlConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.access_control_configuration_name
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.error_message
    import aws_sdk_kendra.types.hierarchical_principal_list
    import aws_sdk_kendra.types.principal_list


class DescribeAccessControlConfigurationResponse(TypedDict):
    name: "aws_sdk_kendra.types.access_control_configuration_name.AccessControlConfigurationName"
    """<p>The name for the access control configuration.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>The description for the access control configuration.</p>"""
    error_message: NotRequired["aws_sdk_kendra.types.error_message.ErrorMessage"]
    """<p>The error message containing details if there are issues processing the access control configuration.</p>"""
    access_control_list: NotRequired[
        "aws_sdk_kendra.types.principal_list.PrincipalList"
    ]
    """<p>Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>"""
    hierarchical_access_control_list: NotRequired[
        "aws_sdk_kendra.types.hierarchical_principal_list.HierarchicalPrincipalList"
    ]
    """<p>The list of <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html\">principal</a> lists that define the hierarchy for which documents users should have access to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccessControlConfigurationResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeAccessControlConfigurationResponse:
    out: DescribeAccessControlConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "DescribeAccessControlConfigurationResponse.name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
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
