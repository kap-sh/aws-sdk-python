"""Generated from Smithy shape ``com.amazonaws.connectparticipant#GetTranscriptRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.contact_id
    import aws_sdk_connectparticipant.types.max_results
    import aws_sdk_connectparticipant.types.next_token
    import aws_sdk_connectparticipant.types.participant_token
    import aws_sdk_connectparticipant.types.scan_direction
    import aws_sdk_connectparticipant.types.sort_key
    import aws_sdk_connectparticipant.types.start_position


class GetTranscriptRequest(TypedDict):
    contact_id: NotRequired["aws_sdk_connectparticipant.types.contact_id.ContactId"]
    """<p>The contactId from the current contact chain for which transcript is needed.</p>"""
    max_results: NotRequired["aws_sdk_connectparticipant.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the page. Default: 10. </p>"""
    next_token: NotRequired["aws_sdk_connectparticipant.types.next_token.NextToken"]
    """<p>The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.</p>"""
    scan_direction: NotRequired[
        "aws_sdk_connectparticipant.types.scan_direction.ScanDirection"
    ]
    """<p>The direction from StartPosition from which to retrieve message. Default: BACKWARD when no StartPosition is provided, FORWARD with StartPosition. </p>"""
    sort_order: NotRequired["aws_sdk_connectparticipant.types.sort_key.SortKey"]
    """<p>The sort order for the records. Default: DESCENDING.</p>"""
    start_position: NotRequired[
        "aws_sdk_connectparticipant.types.start_position.StartPosition"
    ]
    """<p>A filtering option for where to start.</p>"""
    connection_token: (
        "aws_sdk_connectparticipant.types.participant_token.ParticipantToken"
    )
    """<p>The authentication token associated with the participant's connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTranscriptRequest) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "scan_direction" in value:
        import aws_sdk_connectparticipant.types.scan_direction

        out["ScanDirection"] = (
            aws_sdk_connectparticipant.types.scan_direction.serialize_json(
                value["scan_direction"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_connectparticipant.types.sort_key

        out["SortOrder"] = aws_sdk_connectparticipant.types.sort_key.serialize_json(
            value["sort_order"]
        )
    if "start_position" in value:
        import aws_sdk_connectparticipant.types.start_position

        out["StartPosition"] = (
            aws_sdk_connectparticipant.types.start_position.serialize_json(
                value["start_position"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTranscriptRequest:
    out: GetTranscriptRequest = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ScanDirection" in data:
        import aws_sdk_connectparticipant.types.scan_direction

        out["scan_direction"] = (
            aws_sdk_connectparticipant.types.scan_direction.deserialize_json(
                data["ScanDirection"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_connectparticipant.types.sort_key

        out["sort_order"] = aws_sdk_connectparticipant.types.sort_key.deserialize_json(
            data["SortOrder"]
        )
    if "StartPosition" in data:
        import aws_sdk_connectparticipant.types.start_position

        out["start_position"] = (
            aws_sdk_connectparticipant.types.start_position.deserialize_json(
                data["StartPosition"]
            )
        )
    return out
