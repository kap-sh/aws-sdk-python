"""Generated from Smithy shape ``com.amazonaws.mgn#Wave``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.wave_aggregated_status
    import aws_sdk_mgn.types.wave_description
    import aws_sdk_mgn.types.wave_id
    import aws_sdk_mgn.types.wave_name


class Wave(TypedDict):
    wave_id: NotRequired["aws_sdk_mgn.types.wave_id.WaveID"]
    """<p>Wave ID.</p>"""
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>Wave ARN.</p>"""
    name: NotRequired["aws_sdk_mgn.types.wave_name.WaveName"]
    """<p>Wave name.</p>"""
    description: NotRequired["aws_sdk_mgn.types.wave_description.WaveDescription"]
    """<p>Wave description.</p>"""
    is_archived: NotRequired["bool"]
    """<p>Wave archival status.</p>"""
    wave_aggregated_status: NotRequired[
        "aws_sdk_mgn.types.wave_aggregated_status.WaveAggregatedStatus"
    ]
    """<p>Wave aggregated status.</p>"""
    creation_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Wave creation dateTime.</p>"""
    last_modified_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Wave last modified dateTime.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Wave tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Wave) -> dict:
    out: dict = {}
    if "wave_id" in value:
        out["waveID"] = value["wave_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "is_archived" in value:
        out["isArchived"] = value["is_archived"]
    if "wave_aggregated_status" in value:
        import aws_sdk_mgn.types.wave_aggregated_status

        out["waveAggregatedStatus"] = (
            aws_sdk_mgn.types.wave_aggregated_status.serialize_json(
                value["wave_aggregated_status"]
            )
        )
    if "creation_date_time" in value:
        out["creationDateTime"] = value["creation_date_time"]
    if "last_modified_date_time" in value:
        out["lastModifiedDateTime"] = value["last_modified_date_time"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Wave:
    out: Wave = {}  # type: ignore[typeddict-item]
    if "waveID" in data:
        out["wave_id"] = data["waveID"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "isArchived" in data:
        out["is_archived"] = data["isArchived"]
    if "waveAggregatedStatus" in data:
        import aws_sdk_mgn.types.wave_aggregated_status

        out["wave_aggregated_status"] = (
            aws_sdk_mgn.types.wave_aggregated_status.deserialize_json(
                data["waveAggregatedStatus"]
            )
        )
    if "creationDateTime" in data:
        out["creation_date_time"] = data["creationDateTime"]
    if "lastModifiedDateTime" in data:
        out["last_modified_date_time"] = data["lastModifiedDateTime"]
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    return out
