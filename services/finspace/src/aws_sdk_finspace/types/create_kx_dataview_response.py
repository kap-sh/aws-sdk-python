"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxDataviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.availability_zone_id
    import aws_sdk_finspace.types.boolean_value
    import aws_sdk_finspace.types.changeset_id
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.kx_az_mode
    import aws_sdk_finspace.types.kx_dataview_name
    import aws_sdk_finspace.types.kx_dataview_segment_configuration_list
    import aws_sdk_finspace.types.kx_dataview_status
    import aws_sdk_finspace.types.timestamp


class CreateKxDataviewResponse(TypedDict, closed=True):
    dataview_name: NotRequired["aws_sdk_finspace.types.kx_dataview_name.KxDataviewName"]
    """<p>A unique identifier for the dataview.</p>"""
    database_name: NotRequired["aws_sdk_finspace.types.database_name.DatabaseName"]
    """<p>The name of the database where you want to create a dataview.</p>"""
    environment_id: NotRequired["aws_sdk_finspace.types.environment_id.EnvironmentId"]
    """<p>A unique identifier for the kdb environment, where you want to create the dataview. </p>"""
    az_mode: NotRequired["aws_sdk_finspace.types.kx_az_mode.KxAzMode"]
    """<p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p> The identifier of the availability zones. </p>"""
    changeset_id: NotRequired["aws_sdk_finspace.types.changeset_id.ChangesetId"]
    """<p>A unique identifier for the changeset.</p>"""
    segment_configurations: NotRequired[
        "aws_sdk_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
    ]
    """<p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>A description of the dataview.</p>"""
    auto_update: "aws_sdk_finspace.types.boolean_value.booleanValue"
    """<p>The option to select whether you want to apply all the future additions and corrections automatically to the dataview when you ingest new changesets. The default value is false.</p>"""
    read_write: "aws_sdk_finspace.types.boolean_value.booleanValue"
    """<p>Returns True if the dataview is created as writeable and False otherwise. </p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p> The timestamp at which the dataview was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p> The last time that the dataview was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000. </p>"""
    status: NotRequired["aws_sdk_finspace.types.kx_dataview_status.KxDataviewStatus"]
    """<p> The status of dataview creation.</p> <ul> <li> <p> <code>CREATING</code> – The dataview creation is in progress.</p> </li> <li> <p> <code>UPDATING</code> – The dataview is in the process of being updated.</p> </li> <li> <p> <code>ACTIVE</code> – The dataview is active.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxDataviewResponse) -> dict:
    out: dict = {}
    if "dataview_name" in value:
        out["dataviewName"] = value["dataview_name"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "az_mode" in value:
        import aws_sdk_finspace.types.kx_az_mode

        out["azMode"] = aws_sdk_finspace.types.kx_az_mode.serialize_json(
            value["az_mode"]
        )
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "segment_configurations" in value:
        import aws_sdk_finspace.types.kx_dataview_segment_configuration_list

        out["segmentConfigurations"] = (
            aws_sdk_finspace.types.kx_dataview_segment_configuration_list.serialize_json(
                value["segment_configurations"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    out["autoUpdate"] = value.get("auto_update", False)
    out["readWrite"] = value.get("read_write", False)
    if "created_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["createdTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_modified_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["lastModifiedTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    if "status" in value:
        import aws_sdk_finspace.types.kx_dataview_status

        out["status"] = aws_sdk_finspace.types.kx_dataview_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> CreateKxDataviewResponse:
    out: CreateKxDataviewResponse = {}  # type: ignore[typeddict-item]
    if "dataviewName" in data:
        out["dataview_name"] = data["dataviewName"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "azMode" in data:
        import aws_sdk_finspace.types.kx_az_mode

        out["az_mode"] = aws_sdk_finspace.types.kx_az_mode.deserialize_json(
            data["azMode"]
        )
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    if "segmentConfigurations" in data:
        import aws_sdk_finspace.types.kx_dataview_segment_configuration_list

        out["segment_configurations"] = (
            aws_sdk_finspace.types.kx_dataview_segment_configuration_list.deserialize_json(
                data["segmentConfigurations"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "autoUpdate" in data:
        out["auto_update"] = data["autoUpdate"]
    else:
        out["auto_update"] = False
    if "readWrite" in data:
        out["read_write"] = data["readWrite"]
    else:
        out["read_write"] = False
    if "createdTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["created_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    if "lastModifiedTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_finspace.types.timestamp.deserialize_json(
                data["lastModifiedTimestamp"]
            )
        )
    if "status" in data:
        import aws_sdk_finspace.types.kx_dataview_status

        out["status"] = aws_sdk_finspace.types.kx_dataview_status.deserialize_json(
            data["status"]
        )
    return out
