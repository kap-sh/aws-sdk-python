"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegionDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.desired_number_of_domain_controllers
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.directory_stage
    import aws_sdk_directory_service.types.directory_vpc_settings
    import aws_sdk_directory_service.types.last_updated_date_time
    import aws_sdk_directory_service.types.launch_time
    import aws_sdk_directory_service.types.region_name
    import aws_sdk_directory_service.types.region_type
    import aws_sdk_directory_service.types.state_last_updated_date_time


class RegionDescription(TypedDict):
    directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>The identifier of the directory.</p>"""
    region_name: NotRequired["aws_sdk_directory_service.types.region_name.RegionName"]
    """<p>The name of the Region. For example, <code>us-east-1</code>.</p>"""
    region_type: NotRequired["aws_sdk_directory_service.types.region_type.RegionType"]
    """<p>Specifies whether the Region is the primary Region or an additional Region.</p>"""
    status: NotRequired[
        "aws_sdk_directory_service.types.directory_stage.DirectoryStage"
    ]
    """<p>The status of the replication process for the specified Region.</p>"""
    vpc_settings: NotRequired[
        "aws_sdk_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
    ]
    desired_number_of_domain_controllers: NotRequired[
        "aws_sdk_directory_service.types.desired_number_of_domain_controllers.DesiredNumberOfDomainControllers"
    ]
    """<p>The desired number of domain controllers in the specified Region for the specified directory.</p>"""
    launch_time: NotRequired["aws_sdk_directory_service.types.launch_time.LaunchTime"]
    """<p>Specifies when the Region replication began.</p>"""
    status_last_updated_date_time: NotRequired[
        "aws_sdk_directory_service.types.state_last_updated_date_time.StateLastUpdatedDateTime"
    ]
    """<p>The date and time that the Region status was last updated.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time that the Region description was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionDescription) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "region_type" in value:
        import aws_sdk_directory_service.types.region_type

        out["RegionType"] = (
            aws_sdk_directory_service.types.region_type.serialize_aws_json_1_1(
                value["region_type"]
            )
        )
    if "status" in value:
        import aws_sdk_directory_service.types.directory_stage

        out["Status"] = (
            aws_sdk_directory_service.types.directory_stage.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "vpc_settings" in value:
        import aws_sdk_directory_service.types.directory_vpc_settings

        out["VpcSettings"] = (
            aws_sdk_directory_service.types.directory_vpc_settings.serialize_aws_json_1_1(
                value["vpc_settings"]
            )
        )
    if "desired_number_of_domain_controllers" in value:
        out["DesiredNumberOfDomainControllers"] = value[
            "desired_number_of_domain_controllers"
        ]
    if "launch_time" in value:
        import aws_sdk_directory_service.types.launch_time

        out["LaunchTime"] = (
            aws_sdk_directory_service.types.launch_time.serialize_aws_json_1_1(
                value["launch_time"]
            )
        )
    if "status_last_updated_date_time" in value:
        import aws_sdk_directory_service.types.state_last_updated_date_time

        out["StatusLastUpdatedDateTime"] = (
            aws_sdk_directory_service.types.state_last_updated_date_time.serialize_aws_json_1_1(
                value["status_last_updated_date_time"]
            )
        )
    if "last_updated_date_time" in value:
        import aws_sdk_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            aws_sdk_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionDescription:
    out: RegionDescription = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "RegionType" in data:
        import aws_sdk_directory_service.types.region_type

        out["region_type"] = (
            aws_sdk_directory_service.types.region_type.deserialize_aws_json_1_1(
                data["RegionType"]
            )
        )
    if "Status" in data:
        import aws_sdk_directory_service.types.directory_stage

        out["status"] = (
            aws_sdk_directory_service.types.directory_stage.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "VpcSettings" in data:
        import aws_sdk_directory_service.types.directory_vpc_settings

        out["vpc_settings"] = (
            aws_sdk_directory_service.types.directory_vpc_settings.deserialize_aws_json_1_1(
                data["VpcSettings"]
            )
        )
    if "DesiredNumberOfDomainControllers" in data:
        out["desired_number_of_domain_controllers"] = data[
            "DesiredNumberOfDomainControllers"
        ]
    if "LaunchTime" in data:
        import aws_sdk_directory_service.types.launch_time

        out["launch_time"] = (
            aws_sdk_directory_service.types.launch_time.deserialize_aws_json_1_1(
                data["LaunchTime"]
            )
        )
    if "StatusLastUpdatedDateTime" in data:
        import aws_sdk_directory_service.types.state_last_updated_date_time

        out["status_last_updated_date_time"] = (
            aws_sdk_directory_service.types.state_last_updated_date_time.deserialize_aws_json_1_1(
                data["StatusLastUpdatedDateTime"]
            )
        )
    if "LastUpdatedDateTime" in data:
        import aws_sdk_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            aws_sdk_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    return out
