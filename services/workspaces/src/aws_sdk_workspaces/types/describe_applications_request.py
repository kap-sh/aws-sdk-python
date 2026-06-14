"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.compute_list
    import aws_sdk_workspaces.types.limit
    import aws_sdk_workspaces.types.operating_system_name_list
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.work_space_application_id_list
    import aws_sdk_workspaces.types.work_space_application_license_type
    import aws_sdk_workspaces.types.work_space_application_owner


class DescribeApplicationsRequest(TypedDict):
    application_ids: NotRequired[
        "aws_sdk_workspaces.types.work_space_application_id_list.WorkSpaceApplicationIdList"
    ]
    """<p>The identifiers of one or more applications.</p>"""
    compute_type_names: NotRequired["aws_sdk_workspaces.types.compute_list.ComputeList"]
    """<p>The compute types supported by the applications.</p>"""
    license_type: NotRequired[
        "aws_sdk_workspaces.types.work_space_application_license_type.WorkSpaceApplicationLicenseType"
    ]
    """<p>The license availability for the applications.</p>"""
    operating_system_names: NotRequired[
        "aws_sdk_workspaces.types.operating_system_name_list.OperatingSystemNameList"
    ]
    """<p>The operating systems supported by the applications.</p>"""
    owner: NotRequired[
        "aws_sdk_workspaces.types.work_space_application_owner.WorkSpaceApplicationOwner"
    ]
    """<p>The owner of the applications.</p>"""
    max_results: NotRequired["aws_sdk_workspaces.types.limit.Limit"]
    """<p>The maximum number of applications to return.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationsRequest) -> dict:
    out: dict = {}
    if "application_ids" in value:
        import aws_sdk_workspaces.types.work_space_application_id_list

        out["ApplicationIds"] = (
            aws_sdk_workspaces.types.work_space_application_id_list.serialize_aws_json_1_1(
                value["application_ids"]
            )
        )
    if "compute_type_names" in value:
        import aws_sdk_workspaces.types.compute_list

        out["ComputeTypeNames"] = (
            aws_sdk_workspaces.types.compute_list.serialize_aws_json_1_1(
                value["compute_type_names"]
            )
        )
    if "license_type" in value:
        import aws_sdk_workspaces.types.work_space_application_license_type

        out["LicenseType"] = (
            aws_sdk_workspaces.types.work_space_application_license_type.serialize_aws_json_1_1(
                value["license_type"]
            )
        )
    if "operating_system_names" in value:
        import aws_sdk_workspaces.types.operating_system_name_list

        out["OperatingSystemNames"] = (
            aws_sdk_workspaces.types.operating_system_name_list.serialize_aws_json_1_1(
                value["operating_system_names"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationsRequest:
    out: DescribeApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationIds" in data:
        import aws_sdk_workspaces.types.work_space_application_id_list

        out["application_ids"] = (
            aws_sdk_workspaces.types.work_space_application_id_list.deserialize_aws_json_1_1(
                data["ApplicationIds"]
            )
        )
    if "ComputeTypeNames" in data:
        import aws_sdk_workspaces.types.compute_list

        out["compute_type_names"] = (
            aws_sdk_workspaces.types.compute_list.deserialize_aws_json_1_1(
                data["ComputeTypeNames"]
            )
        )
    if "LicenseType" in data:
        import aws_sdk_workspaces.types.work_space_application_license_type

        out["license_type"] = (
            aws_sdk_workspaces.types.work_space_application_license_type.deserialize_aws_json_1_1(
                data["LicenseType"]
            )
        )
    if "OperatingSystemNames" in data:
        import aws_sdk_workspaces.types.operating_system_name_list

        out["operating_system_names"] = (
            aws_sdk_workspaces.types.operating_system_name_list.deserialize_aws_json_1_1(
                data["OperatingSystemNames"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
