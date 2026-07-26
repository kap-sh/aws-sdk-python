"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.desired_number_of_domain_controllers
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.directory_stage
    import capo_directory_service.types.directory_vpc_settings
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.launch_time
    import capo_directory_service.types.region_name
    import capo_directory_service.types.region_type
    import capo_directory_service.types.state_last_updated_date_time


class RegionDescription(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory.</p>"""
    region_name: NotRequired["capo_directory_service.types.region_name.RegionName"]
    """<p>The name of the Region. For example, <code>us-east-1</code>.</p>"""
    region_type: NotRequired["capo_directory_service.types.region_type.RegionType"]
    """<p>Specifies whether the Region is the primary Region or an additional Region.</p>"""
    status: NotRequired["capo_directory_service.types.directory_stage.DirectoryStage"]
    """<p>The status of the replication process for the specified Region.</p>"""
    vpc_settings: NotRequired[
        "capo_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
    ]
    desired_number_of_domain_controllers: NotRequired[
        "capo_directory_service.types.desired_number_of_domain_controllers.DesiredNumberOfDomainControllers"
    ]
    """<p>The desired number of domain controllers in the specified Region for the specified directory.</p>"""
    launch_time: NotRequired["capo_directory_service.types.launch_time.LaunchTime"]
    """<p>Specifies when the Region replication began.</p>"""
    status_last_updated_date_time: NotRequired[
        "capo_directory_service.types.state_last_updated_date_time.StateLastUpdatedDateTime"
    ]
    """<p>The date and time that the Region status was last updated.</p>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
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
        import capo_directory_service.types.region_type

        out["RegionType"] = (
            capo_directory_service.types.region_type.serialize_aws_json_1_1(
                value["region_type"]
            )
        )
    if "status" in value:
        import capo_directory_service.types.directory_stage

        out["Status"] = (
            capo_directory_service.types.directory_stage.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "vpc_settings" in value:
        import capo_directory_service.types.directory_vpc_settings

        out["VpcSettings"] = (
            capo_directory_service.types.directory_vpc_settings.serialize_aws_json_1_1(
                value["vpc_settings"]
            )
        )
    if "desired_number_of_domain_controllers" in value:
        out["DesiredNumberOfDomainControllers"] = value[
            "desired_number_of_domain_controllers"
        ]
    if "launch_time" in value:
        import capo_directory_service.types.launch_time

        out["LaunchTime"] = (
            capo_directory_service.types.launch_time.serialize_aws_json_1_1(
                value["launch_time"]
            )
        )
    if "status_last_updated_date_time" in value:
        import capo_directory_service.types.state_last_updated_date_time

        out["StatusLastUpdatedDateTime"] = (
            capo_directory_service.types.state_last_updated_date_time.serialize_aws_json_1_1(
                value["status_last_updated_date_time"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
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
        import capo_directory_service.types.region_type

        out["region_type"] = (
            capo_directory_service.types.region_type.deserialize_aws_json_1_1(
                data["RegionType"]
            )
        )
    if "Status" in data:
        import capo_directory_service.types.directory_stage

        out["status"] = (
            capo_directory_service.types.directory_stage.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "VpcSettings" in data:
        import capo_directory_service.types.directory_vpc_settings

        out["vpc_settings"] = (
            capo_directory_service.types.directory_vpc_settings.deserialize_aws_json_1_1(
                data["VpcSettings"]
            )
        )
    if "DesiredNumberOfDomainControllers" in data:
        out["desired_number_of_domain_controllers"] = data[
            "DesiredNumberOfDomainControllers"
        ]
    if "LaunchTime" in data:
        import capo_directory_service.types.launch_time

        out["launch_time"] = (
            capo_directory_service.types.launch_time.deserialize_aws_json_1_1(
                data["LaunchTime"]
            )
        )
    if "StatusLastUpdatedDateTime" in data:
        import capo_directory_service.types.state_last_updated_date_time

        out["status_last_updated_date_time"] = (
            capo_directory_service.types.state_last_updated_date_time.deserialize_aws_json_1_1(
                data["StatusLastUpdatedDateTime"]
            )
        )
    if "LastUpdatedDateTime" in data:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    return out
