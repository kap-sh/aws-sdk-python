"""Generated from Smithy shape ``com.amazonaws.mgn#Application``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.application_aggregated_status
    import aws_sdk_mgn.types.application_description
    import aws_sdk_mgn.types.application_id
    import aws_sdk_mgn.types.application_name
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.wave_id


class Application(TypedDict):
    application_id: NotRequired["aws_sdk_mgn.types.application_id.ApplicationID"]
    """<p>Application ID.</p>"""
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>Application ARN.</p>"""
    name: NotRequired["aws_sdk_mgn.types.application_name.ApplicationName"]
    """<p>Application name.</p>"""
    description: NotRequired[
        "aws_sdk_mgn.types.application_description.ApplicationDescription"
    ]
    """<p>Application description.</p>"""
    is_archived: NotRequired["bool"]
    """<p>Application archival status.</p>"""
    application_aggregated_status: NotRequired[
        "aws_sdk_mgn.types.application_aggregated_status.ApplicationAggregatedStatus"
    ]
    """<p>Application aggregated status.</p>"""
    creation_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Application creation dateTime.</p>"""
    last_modified_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Application last modified dateTime.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Application tags.</p>"""
    wave_id: NotRequired["aws_sdk_mgn.types.wave_id.WaveID"]
    """<p>Application wave ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Application) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationID"] = value["application_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "is_archived" in value:
        out["isArchived"] = value["is_archived"]
    if "application_aggregated_status" in value:
        import aws_sdk_mgn.types.application_aggregated_status

        out["applicationAggregatedStatus"] = (
            aws_sdk_mgn.types.application_aggregated_status.serialize_json(
                value["application_aggregated_status"]
            )
        )
    if "creation_date_time" in value:
        out["creationDateTime"] = value["creation_date_time"]
    if "last_modified_date_time" in value:
        out["lastModifiedDateTime"] = value["last_modified_date_time"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "wave_id" in value:
        out["waveID"] = value["wave_id"]
    return out


def deserialize_json(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "applicationID" in data:
        out["application_id"] = data["applicationID"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "isArchived" in data:
        out["is_archived"] = data["isArchived"]
    if "applicationAggregatedStatus" in data:
        import aws_sdk_mgn.types.application_aggregated_status

        out["application_aggregated_status"] = (
            aws_sdk_mgn.types.application_aggregated_status.deserialize_json(
                data["applicationAggregatedStatus"]
            )
        )
    if "creationDateTime" in data:
        out["creation_date_time"] = data["creationDateTime"]
    if "lastModifiedDateTime" in data:
        out["last_modified_date_time"] = data["lastModifiedDateTime"]
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "waveID" in data:
        out["wave_id"] = data["waveID"]
    return out
