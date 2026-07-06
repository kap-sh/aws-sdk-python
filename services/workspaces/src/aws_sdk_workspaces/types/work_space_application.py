"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.compute_list
    import aws_sdk_workspaces.types.non_empty_string
    import aws_sdk_workspaces.types.operating_system_name_list
    import aws_sdk_workspaces.types.string2048
    import aws_sdk_workspaces.types.timestamp
    import aws_sdk_workspaces.types.work_space_application_id
    import aws_sdk_workspaces.types.work_space_application_license_type
    import aws_sdk_workspaces.types.work_space_application_owner
    import aws_sdk_workspaces.types.work_space_application_state


class WorkSpaceApplication(TypedDict, closed=True):
    application_id: NotRequired[
        "aws_sdk_workspaces.types.work_space_application_id.WorkSpaceApplicationId"
    ]
    """<p>The identifier of the application.</p>"""
    created: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The time the application is created.</p>"""
    description: NotRequired["aws_sdk_workspaces.types.string2048.String2048"]
    """<p>The description of the WorkSpace application.</p>"""
    license_type: NotRequired[
        "aws_sdk_workspaces.types.work_space_application_license_type.WorkSpaceApplicationLicenseType"
    ]
    """<p>The license availability for the applications.</p>"""
    name: NotRequired["aws_sdk_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The name of the WorkSpace application.</p>"""
    owner: NotRequired[
        "aws_sdk_workspaces.types.work_space_application_owner.WorkSpaceApplicationOwner"
    ]
    """<p>The owner of the WorkSpace application.</p>"""
    state: NotRequired[
        "aws_sdk_workspaces.types.work_space_application_state.WorkSpaceApplicationState"
    ]
    """<p>The status of WorkSpace application.</p>"""
    supported_compute_type_names: NotRequired[
        "aws_sdk_workspaces.types.compute_list.ComputeList"
    ]
    """<p>The supported compute types of the WorkSpace application.</p>"""
    supported_operating_system_names: NotRequired[
        "aws_sdk_workspaces.types.operating_system_name_list.OperatingSystemNameList"
    ]
    """<p>The supported operating systems of the WorkSpace application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceApplication) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "created" in value:
        import aws_sdk_workspaces.types.timestamp

        out["Created"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "license_type" in value:
        import aws_sdk_workspaces.types.work_space_application_license_type

        out["LicenseType"] = (
            aws_sdk_workspaces.types.work_space_application_license_type.serialize_aws_json_1_1(
                value["license_type"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "state" in value:
        import aws_sdk_workspaces.types.work_space_application_state

        out["State"] = (
            aws_sdk_workspaces.types.work_space_application_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "supported_compute_type_names" in value:
        import aws_sdk_workspaces.types.compute_list

        out["SupportedComputeTypeNames"] = (
            aws_sdk_workspaces.types.compute_list.serialize_aws_json_1_1(
                value["supported_compute_type_names"]
            )
        )
    if "supported_operating_system_names" in value:
        import aws_sdk_workspaces.types.operating_system_name_list

        out["SupportedOperatingSystemNames"] = (
            aws_sdk_workspaces.types.operating_system_name_list.serialize_aws_json_1_1(
                value["supported_operating_system_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkSpaceApplication:
    out: WorkSpaceApplication = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "Created" in data:
        import aws_sdk_workspaces.types.timestamp

        out["created"] = aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["Created"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "LicenseType" in data:
        import aws_sdk_workspaces.types.work_space_application_license_type

        out["license_type"] = (
            aws_sdk_workspaces.types.work_space_application_license_type.deserialize_aws_json_1_1(
                data["LicenseType"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "State" in data:
        import aws_sdk_workspaces.types.work_space_application_state

        out["state"] = (
            aws_sdk_workspaces.types.work_space_application_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "SupportedComputeTypeNames" in data:
        import aws_sdk_workspaces.types.compute_list

        out["supported_compute_type_names"] = (
            aws_sdk_workspaces.types.compute_list.deserialize_aws_json_1_1(
                data["SupportedComputeTypeNames"]
            )
        )
    if "SupportedOperatingSystemNames" in data:
        import aws_sdk_workspaces.types.operating_system_name_list

        out["supported_operating_system_names"] = (
            aws_sdk_workspaces.types.operating_system_name_list.deserialize_aws_json_1_1(
                data["SupportedOperatingSystemNames"]
            )
        )
    return out
