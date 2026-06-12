"""Generated from Smithy shape ``com.amazonaws.ivs#ListRecordingConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.pagination_token
    import aws_sdk_ivs.types.recording_configuration_list


class ListRecordingConfigurationsResponse(TypedDict):
    recording_configurations: (
        "aws_sdk_ivs.types.recording_configuration_list.RecordingConfigurationList"
    )
    """<p>List of the matching recording configurations.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more recording configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecordingConfigurationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.recording_configuration_list

    out["recordingConfigurations"] = (
        aws_sdk_ivs.types.recording_configuration_list.serialize_json(
            value["recording_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecordingConfigurationsResponse:
    out: ListRecordingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "recordingConfigurations" in data:
        import aws_sdk_ivs.types.recording_configuration_list

        out["recording_configurations"] = (
            aws_sdk_ivs.types.recording_configuration_list.deserialize_json(
                data["recordingConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListRecordingConfigurationsResponse.recording_configurations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
