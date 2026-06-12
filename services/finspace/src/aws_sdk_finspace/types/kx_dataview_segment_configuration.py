"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviewSegmentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.boolean_value
    import aws_sdk_finspace.types.kx_volume_name
    import aws_sdk_finspace.types.segment_configuration_db_path_list


class KxDataviewSegmentConfiguration(TypedDict):
    db_paths: "aws_sdk_finspace.types.segment_configuration_db_path_list.SegmentConfigurationDbPathList"
    """<p> The database path of the data that you want to place on each selected volume for the segment. Each segment must have a unique database path for each volume.</p>"""
    volume_name: "aws_sdk_finspace.types.kx_volume_name.KxVolumeName"
    """<p> The name of the volume where you want to add data. </p>"""
    on_demand: "aws_sdk_finspace.types.boolean_value.booleanValue"
    """<p>Enables on-demand caching on the selected database path when a particular file or a column of the database is accessed. When on demand caching is <b>True</b>, dataviews perform minimal loading of files on the filesystem as needed. When it is set to <b>False</b>, everything is cached. The default value is <b>False</b>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxDataviewSegmentConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_finspace.types.segment_configuration_db_path_list

    out["dbPaths"] = (
        aws_sdk_finspace.types.segment_configuration_db_path_list.serialize_json(
            value["db_paths"]
        )
    )
    out["volumeName"] = value["volume_name"]
    out["onDemand"] = value.get("on_demand", False)
    return out


def deserialize_json(data: dict) -> KxDataviewSegmentConfiguration:
    out: KxDataviewSegmentConfiguration = {}  # type: ignore[typeddict-item]
    if "dbPaths" in data:
        import aws_sdk_finspace.types.segment_configuration_db_path_list

        out["db_paths"] = (
            aws_sdk_finspace.types.segment_configuration_db_path_list.deserialize_json(
                data["dbPaths"]
            )
        )
    else:
        raise DeserializationError("KxDataviewSegmentConfiguration.db_paths required")
    if "volumeName" in data:
        out["volume_name"] = data["volumeName"]
    else:
        raise DeserializationError(
            "KxDataviewSegmentConfiguration.volume_name required"
        )
    if "onDemand" in data:
        out["on_demand"] = data["onDemand"]
    else:
        out["on_demand"] = False
    return out
