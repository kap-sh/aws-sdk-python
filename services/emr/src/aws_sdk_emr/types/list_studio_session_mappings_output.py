"""Generated from Smithy shape ``com.amazonaws.emr#ListStudioSessionMappingsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.marker
    import aws_sdk_emr.types.session_mapping_summary_list


class ListStudioSessionMappingsOutput(TypedDict):
    session_mappings: NotRequired[
        "aws_sdk_emr.types.session_mapping_summary_list.SessionMappingSummaryList"
    ]
    """<p>A list of session mapping summary objects. Each object includes session mapping details such as creation time, identity type (user or group), and Amazon EMR Studio ID.</p>"""
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStudioSessionMappingsOutput) -> dict:
    out: dict = {}
    if "session_mappings" in value:
        import aws_sdk_emr.types.session_mapping_summary_list

        out["SessionMappings"] = (
            aws_sdk_emr.types.session_mapping_summary_list.serialize_aws_json_1_1(
                value["session_mappings"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStudioSessionMappingsOutput:
    out: ListStudioSessionMappingsOutput = {}  # type: ignore[typeddict-item]
    if "SessionMappings" in data:
        import aws_sdk_emr.types.session_mapping_summary_list

        out["session_mappings"] = (
            aws_sdk_emr.types.session_mapping_summary_list.deserialize_aws_json_1_1(
                data["SessionMappings"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
