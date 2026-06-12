"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListRemoteAccessSessionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.remote_access_sessions


class ListRemoteAccessSessionsResult(TypedDict):
    remote_access_sessions: NotRequired[
        "aws_sdk_device_farm.types.remote_access_sessions.RemoteAccessSessions"
    ]
    """<p>A container that represents the metadata from the service about each remote access session you are requesting.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRemoteAccessSessionsResult) -> dict:
    out: dict = {}
    if "remote_access_sessions" in value:
        import aws_sdk_device_farm.types.remote_access_sessions

        out["remoteAccessSessions"] = (
            aws_sdk_device_farm.types.remote_access_sessions.serialize_aws_json_1_1(
                value["remote_access_sessions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRemoteAccessSessionsResult:
    out: ListRemoteAccessSessionsResult = {}  # type: ignore[typeddict-item]
    if "remoteAccessSessions" in data:
        import aws_sdk_device_farm.types.remote_access_sessions

        out["remote_access_sessions"] = (
            aws_sdk_device_farm.types.remote_access_sessions.deserialize_aws_json_1_1(
                data["remoteAccessSessions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
