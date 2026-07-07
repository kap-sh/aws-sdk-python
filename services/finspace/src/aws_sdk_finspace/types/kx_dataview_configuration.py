"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviewConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.changeset_id
    import aws_sdk_finspace.types.kx_dataview_name
    import aws_sdk_finspace.types.kx_dataview_segment_configuration_list
    import aws_sdk_finspace.types.version_id


class KxDataviewConfiguration(TypedDict, closed=True):
    dataview_name: NotRequired["aws_sdk_finspace.types.kx_dataview_name.KxDataviewName"]
    """<p> The unique identifier of the dataview.</p>"""
    dataview_version_id: NotRequired["aws_sdk_finspace.types.version_id.VersionId"]
    """<p> The version of the dataview corresponding to a given changeset. </p>"""
    changeset_id: NotRequired["aws_sdk_finspace.types.changeset_id.ChangesetId"]
    """<p>A unique identifier for the changeset.</p>"""
    segment_configurations: NotRequired[
        "aws_sdk_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
    ]
    """<p> The db path and volume configuration for the segmented database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxDataviewConfiguration) -> dict:
    out: dict = {}
    if "dataview_name" in value:
        out["dataviewName"] = value["dataview_name"]
    if "dataview_version_id" in value:
        out["dataviewVersionId"] = value["dataview_version_id"]
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "segment_configurations" in value:
        import aws_sdk_finspace.types.kx_dataview_segment_configuration_list

        out["segmentConfigurations"] = (
            aws_sdk_finspace.types.kx_dataview_segment_configuration_list.serialize_json(
                value["segment_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> KxDataviewConfiguration:
    out: KxDataviewConfiguration = {}  # type: ignore[typeddict-item]
    if "dataviewName" in data:
        out["dataview_name"] = data["dataviewName"]
    if "dataviewVersionId" in data:
        out["dataview_version_id"] = data["dataviewVersionId"]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    if "segmentConfigurations" in data:
        import aws_sdk_finspace.types.kx_dataview_segment_configuration_list

        out["segment_configurations"] = (
            aws_sdk_finspace.types.kx_dataview_segment_configuration_list.deserialize_json(
                data["segmentConfigurations"]
            )
        )
    return out
