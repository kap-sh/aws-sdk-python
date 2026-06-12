"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.assigned_group_patterns_list
    import aws_sdk_sagemaker.types.partner_app_admin_user_list
    import aws_sdk_sagemaker.types.partner_app_arguments
    import aws_sdk_sagemaker.types.role_group_assignments_list


class PartnerAppConfig(TypedDict):
    admin_users: NotRequired[
        "aws_sdk_sagemaker.types.partner_app_admin_user_list.PartnerAppAdminUserList"
    ]
    """<p>The list of users that are given admin access to the SageMaker Partner AI App.</p>"""
    arguments: NotRequired[
        "aws_sdk_sagemaker.types.partner_app_arguments.PartnerAppArguments"
    ]
    """<p>This is a map of required inputs for a SageMaker Partner AI App. Based on the application type, the map is populated with a key and value pair that is specific to the user and application.</p>"""
    assigned_group_patterns: NotRequired[
        "aws_sdk_sagemaker.types.assigned_group_patterns_list.AssignedGroupPatternsList"
    ]
    """<p>A list of Amazon Web Services IAM Identity Center group patterns that can access the SageMaker Partner AI App. Group names support wildcard matching using <code>*</code>. An empty list indicates the app will not use Identity Center group features. All groups specified in <code>RoleGroupAssignments</code> must match patterns in this list.</p>"""
    role_group_assignments: NotRequired[
        "aws_sdk_sagemaker.types.role_group_assignments_list.RoleGroupAssignmentsList"
    ]
    """<p>A map of in-app roles to Amazon Web Services IAM Identity Center group patterns. Groups assigned to specific roles receive those permissions, while groups in <code>AssignedGroupPatterns</code> but not in this map receive default in-app role depending on app type. Group patterns support wildcard matching using <code>*</code>. Currently supported by Fiddler version 1.3 and later with roles: <code>ORG_MEMBER</code> (default) and <code>ORG_ADMIN</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppConfig) -> dict:
    out: dict = {}
    if "admin_users" in value:
        import aws_sdk_sagemaker.types.partner_app_admin_user_list

        out["AdminUsers"] = (
            aws_sdk_sagemaker.types.partner_app_admin_user_list.serialize_aws_json_1_1(
                value["admin_users"]
            )
        )
    if "arguments" in value:
        import aws_sdk_sagemaker.types.partner_app_arguments

        out["Arguments"] = (
            aws_sdk_sagemaker.types.partner_app_arguments.serialize_aws_json_1_1(
                value["arguments"]
            )
        )
    if "assigned_group_patterns" in value:
        import aws_sdk_sagemaker.types.assigned_group_patterns_list

        out["AssignedGroupPatterns"] = (
            aws_sdk_sagemaker.types.assigned_group_patterns_list.serialize_aws_json_1_1(
                value["assigned_group_patterns"]
            )
        )
    if "role_group_assignments" in value:
        import aws_sdk_sagemaker.types.role_group_assignments_list

        out["RoleGroupAssignments"] = (
            aws_sdk_sagemaker.types.role_group_assignments_list.serialize_aws_json_1_1(
                value["role_group_assignments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartnerAppConfig:
    out: PartnerAppConfig = {}  # type: ignore[typeddict-item]
    if "AdminUsers" in data:
        import aws_sdk_sagemaker.types.partner_app_admin_user_list

        out["admin_users"] = (
            aws_sdk_sagemaker.types.partner_app_admin_user_list.deserialize_aws_json_1_1(
                data["AdminUsers"]
            )
        )
    if "Arguments" in data:
        import aws_sdk_sagemaker.types.partner_app_arguments

        out["arguments"] = (
            aws_sdk_sagemaker.types.partner_app_arguments.deserialize_aws_json_1_1(
                data["Arguments"]
            )
        )
    if "AssignedGroupPatterns" in data:
        import aws_sdk_sagemaker.types.assigned_group_patterns_list

        out["assigned_group_patterns"] = (
            aws_sdk_sagemaker.types.assigned_group_patterns_list.deserialize_aws_json_1_1(
                data["AssignedGroupPatterns"]
            )
        )
    if "RoleGroupAssignments" in data:
        import aws_sdk_sagemaker.types.role_group_assignments_list

        out["role_group_assignments"] = (
            aws_sdk_sagemaker.types.role_group_assignments_list.deserialize_aws_json_1_1(
                data["RoleGroupAssignments"]
            )
        )
    return out
