"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxDataviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.availability_zone_id
    import capo_finspace.types.boolean_value
    import capo_finspace.types.changeset_id
    import capo_finspace.types.database_name
    import capo_finspace.types.description
    import capo_finspace.types.environment_id
    import capo_finspace.types.kx_az_mode
    import capo_finspace.types.kx_dataview_active_version_list
    import capo_finspace.types.kx_dataview_name
    import capo_finspace.types.kx_dataview_segment_configuration_list
    import capo_finspace.types.kx_dataview_status
    import capo_finspace.types.kx_dataview_status_reason
    import capo_finspace.types.timestamp


class GetKxDataviewResponse(TypedDict, closed=True):
    database_name: NotRequired["capo_finspace.types.database_name.DatabaseName"]
    """<p> The name of the database where you created the dataview.</p>"""
    dataview_name: NotRequired["capo_finspace.types.kx_dataview_name.KxDataviewName"]
    """<p>A unique identifier for the dataview.</p>"""
    az_mode: NotRequired["capo_finspace.types.kx_az_mode.KxAzMode"]
    """<p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>"""
    availability_zone_id: NotRequired[
        "capo_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p> The identifier of the availability zones. </p>"""
    changeset_id: NotRequired["capo_finspace.types.changeset_id.ChangesetId"]
    """<p> A unique identifier of the changeset that you want to use to ingest data. </p>"""
    segment_configurations: NotRequired[
        "capo_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
    ]
    """<p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>"""
    active_versions: NotRequired[
        "capo_finspace.types.kx_dataview_active_version_list.KxDataviewActiveVersionList"
    ]
    """<p> The current active changeset versions of the database on the given dataview. </p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>A description of the dataview.</p>"""
    auto_update: "capo_finspace.types.boolean_value.booleanValue"
    """<p>The option to specify whether you want to apply all the future additions and corrections automatically to the dataview when new changesets are ingested. The default value is false.</p>"""
    read_write: "capo_finspace.types.boolean_value.booleanValue"
    """<p>Returns True if the dataview is created as writeable and False otherwise. </p>"""
    environment_id: NotRequired["capo_finspace.types.environment_id.EnvironmentId"]
    """<p>A unique identifier for the kdb environment, from where you want to retrieve the dataview details.</p>"""
    created_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the dataview was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p> The last time that the dataview was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000. </p>"""
    status: NotRequired["capo_finspace.types.kx_dataview_status.KxDataviewStatus"]
    """<p> The status of dataview creation.</p> <ul> <li> <p> <code>CREATING</code> – The dataview creation is in progress.</p> </li> <li> <p> <code>UPDATING</code> – The dataview is in the process of being updated.</p> </li> <li> <p> <code>ACTIVE</code> – The dataview is active.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_finspace.types.kx_dataview_status_reason.KxDataviewStatusReason"
    ]
    """<p> The error message when a failed state occurs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxDataviewResponse) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "dataview_name" in value:
        out["dataviewName"] = value["dataview_name"]
    if "az_mode" in value:
        import capo_finspace.types.kx_az_mode

        out["azMode"] = capo_finspace.types.kx_az_mode.serialize_json(value["az_mode"])
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "segment_configurations" in value:
        import capo_finspace.types.kx_dataview_segment_configuration_list

        out["segmentConfigurations"] = (
            capo_finspace.types.kx_dataview_segment_configuration_list.serialize_json(
                value["segment_configurations"]
            )
        )
    if "active_versions" in value:
        import capo_finspace.types.kx_dataview_active_version_list

        out["activeVersions"] = (
            capo_finspace.types.kx_dataview_active_version_list.serialize_json(
                value["active_versions"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    out["autoUpdate"] = value.get("auto_update", False)
    out["readWrite"] = value.get("read_write", False)
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "created_timestamp" in value:
        import capo_finspace.types.timestamp

        out["createdTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_modified_timestamp" in value:
        import capo_finspace.types.timestamp

        out["lastModifiedTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    if "status" in value:
        import capo_finspace.types.kx_dataview_status

        out["status"] = capo_finspace.types.kx_dataview_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> GetKxDataviewResponse:
    out: GetKxDataviewResponse = {}  # type: ignore[typeddict-item]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "dataviewName" in data:
        out["dataview_name"] = data["dataviewName"]
    if "azMode" in data:
        import capo_finspace.types.kx_az_mode

        out["az_mode"] = capo_finspace.types.kx_az_mode.deserialize_json(data["azMode"])
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    if "segmentConfigurations" in data:
        import capo_finspace.types.kx_dataview_segment_configuration_list

        out["segment_configurations"] = (
            capo_finspace.types.kx_dataview_segment_configuration_list.deserialize_json(
                data["segmentConfigurations"]
            )
        )
    if "activeVersions" in data:
        import capo_finspace.types.kx_dataview_active_version_list

        out["active_versions"] = (
            capo_finspace.types.kx_dataview_active_version_list.deserialize_json(
                data["activeVersions"]
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
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "createdTimestamp" in data:
        import capo_finspace.types.timestamp

        out["created_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    if "lastModifiedTimestamp" in data:
        import capo_finspace.types.timestamp

        out["last_modified_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["lastModifiedTimestamp"]
        )
    if "status" in data:
        import capo_finspace.types.kx_dataview_status

        out["status"] = capo_finspace.types.kx_dataview_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
