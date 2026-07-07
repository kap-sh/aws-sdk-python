"""Generated from Smithy shape ``com.amazonaws.qapps#ListQAppSessionDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.q_app_session_data_list
    import aws_sdk_qapps.types.uuid


class ListQAppSessionDataOutput(TypedDict, closed=True):
    session_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App data collection session.</p>"""
    session_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Q App data collection session.</p>"""
    session_data: NotRequired[
        "aws_sdk_qapps.types.q_app_session_data_list.QAppSessionDataList"
    ]
    """<p>The collected responses of a Q App session.</p>"""
    next_token: NotRequired["str"]
    """<p> The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQAppSessionDataOutput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    if "session_data" in value:
        import aws_sdk_qapps.types.q_app_session_data_list

        out["sessionData"] = aws_sdk_qapps.types.q_app_session_data_list.serialize_json(
            value["session_data"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQAppSessionDataOutput:
    out: ListQAppSessionDataOutput = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("ListQAppSessionDataOutput.session_id required")
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("ListQAppSessionDataOutput.session_arn required")
    if "sessionData" in data:
        import aws_sdk_qapps.types.q_app_session_data_list

        out["session_data"] = (
            aws_sdk_qapps.types.q_app_session_data_list.deserialize_json(
                data["sessionData"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
