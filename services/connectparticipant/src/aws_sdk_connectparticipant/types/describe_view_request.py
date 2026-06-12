"""Generated from Smithy shape ``com.amazonaws.connectparticipant#DescribeViewRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.participant_token
    import aws_sdk_connectparticipant.types.view_token


class DescribeViewRequest(TypedDict):
    view_token: "aws_sdk_connectparticipant.types.view_token.ViewToken"
    """<p>An encrypted token originating from the interactive message of a ShowView block operation. Represents the desired view.</p>"""
    connection_token: (
        "aws_sdk_connectparticipant.types.participant_token.ParticipantToken"
    )
    """<p>The connection token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeViewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeViewRequest:
    out: DescribeViewRequest = {}  # type: ignore[typeddict-item]
    return out
