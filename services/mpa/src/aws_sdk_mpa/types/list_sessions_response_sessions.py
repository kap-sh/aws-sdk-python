"""Generated from Smithy shape ``com.amazonaws.mpa#ListSessionsResponseSessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.list_sessions_response_session

ListSessionsResponseSessions: TypeAlias = list[
    "aws_sdk_mpa.types.list_sessions_response_session.ListSessionsResponseSession"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponseSessions) -> list:
    import aws_sdk_mpa.types.list_sessions_response_session

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mpa.types.list_sessions_response_session.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListSessionsResponseSessions:
    import aws_sdk_mpa.types.list_sessions_response_session

    out: ListSessionsResponseSessions = []
    for item in data:
        out.append(
            aws_sdk_mpa.types.list_sessions_response_session.deserialize_json(item)
        )
    return out
