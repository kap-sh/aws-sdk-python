"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxDataviewRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.availability_zone_id
    import aws_sdk_finspace.types.boolean_value
    import aws_sdk_finspace.types.changeset_id
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.kx_az_mode
    import aws_sdk_finspace.types.kx_dataview_name
    import aws_sdk_finspace.types.kx_dataview_segment_configuration_list
    import aws_sdk_finspace.types.tag_map


class CreateKxDataviewRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment, where you want to create the dataview. </p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p> The name of the database where you want to create a dataview. </p>"""
    dataview_name: "aws_sdk_finspace.types.kx_dataview_name.KxDataviewName"
    """<p>A unique identifier for the dataview.</p>"""
    az_mode: "aws_sdk_finspace.types.kx_az_mode.KxAzMode"
    """<p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p> The identifier of the availability zones. </p>"""
    changeset_id: NotRequired["aws_sdk_finspace.types.changeset_id.ChangesetId"]
    """<p> A unique identifier of the changeset that you want to use to ingest data. </p>"""
    segment_configurations: NotRequired[
        "aws_sdk_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
    ]
    """<p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>"""
    auto_update: "aws_sdk_finspace.types.boolean_value.booleanValue"
    """<p>The option to specify whether you want to apply all the future additions and corrections automatically to the dataview, when you ingest new changesets. The default value is false.</p>"""
    read_write: "aws_sdk_finspace.types.boolean_value.booleanValue"
    """<p> The option to specify whether you want to make the dataview writable to perform database maintenance. The following are some considerations related to writable dataviews. </p> <ul> <li> <p>You cannot create partial writable dataviews. When you create writeable dataviews you must provide the entire database path.</p> </li> <li> <p>You cannot perform updates on a writeable dataview. Hence, <code>autoUpdate</code> must be set as <b>False</b> if <code>readWrite</code> is <b>True</b> for a dataview.</p> </li> <li> <p>You must also use a unique volume for creating a writeable dataview. So, if you choose a volume that is already in use by another dataview, the dataview creation fails.</p> </li> <li> <p>Once you create a dataview as writeable, you cannot change it to read-only. So, you cannot update the <code>readWrite</code> parameter later.</p> </li> </ul>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>A description of the dataview.</p>"""
    tags: NotRequired["aws_sdk_finspace.types.tag_map.TagMap"]
    """<p> A list of key-value pairs to label the dataview. You can add up to 50 tags to a dataview. </p>"""
    client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxDataviewRequest) -> dict:
    out: dict = {}
    out["dataviewName"] = value["dataview_name"]
    import aws_sdk_finspace.types.kx_az_mode

    out["azMode"] = aws_sdk_finspace.types.kx_az_mode.serialize_json(value["az_mode"])
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
    out["autoUpdate"] = value.get("auto_update", False)
    out["readWrite"] = value.get("read_write", False)
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateKxDataviewRequest:
    out: CreateKxDataviewRequest = {}  # type: ignore[typeddict-item]
    if "dataviewName" in data:
        out["dataview_name"] = data["dataviewName"]
    else:
        raise DeserializationError("CreateKxDataviewRequest.dataview_name required")
    if "azMode" in data:
        import aws_sdk_finspace.types.kx_az_mode

        out["az_mode"] = aws_sdk_finspace.types.kx_az_mode.deserialize_json(
            data["azMode"]
        )
    else:
        raise DeserializationError("CreateKxDataviewRequest.az_mode required")
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
    if "autoUpdate" in data:
        out["auto_update"] = data["autoUpdate"]
    else:
        out["auto_update"] = False
    if "readWrite" in data:
        out["read_write"] = data["readWrite"]
    else:
        out["read_write"] = False
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateKxDataviewRequest.client_token required")
    return out
