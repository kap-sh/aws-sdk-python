"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetRemoteAccessSessionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.remote_access_session


class GetRemoteAccessSessionResult(TypedDict, closed=True):
    remote_access_session: NotRequired[
        "aws_sdk_device_farm.types.remote_access_session.RemoteAccessSession"
    ]
    """<p>A container that lists detailed information about the remote access session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRemoteAccessSessionResult) -> dict:
    out: dict = {}
    if "remote_access_session" in value:
        import aws_sdk_device_farm.types.remote_access_session

        out["remoteAccessSession"] = (
            aws_sdk_device_farm.types.remote_access_session.serialize_aws_json_1_1(
                value["remote_access_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRemoteAccessSessionResult:
    out: GetRemoteAccessSessionResult = {}  # type: ignore[typeddict-item]
    if "remoteAccessSession" in data:
        import aws_sdk_device_farm.types.remote_access_session

        out["remote_access_session"] = (
            aws_sdk_device_farm.types.remote_access_session.deserialize_aws_json_1_1(
                data["remoteAccessSession"]
            )
        )
    return out
