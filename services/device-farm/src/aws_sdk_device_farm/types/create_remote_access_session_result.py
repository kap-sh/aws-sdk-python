"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateRemoteAccessSessionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.remote_access_session


class CreateRemoteAccessSessionResult(TypedDict):
    remote_access_session: NotRequired[
        "aws_sdk_device_farm.types.remote_access_session.RemoteAccessSession"
    ]
    """<p>A container that describes the remote access session when the request to create a remote access session is sent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRemoteAccessSessionResult) -> dict:
    out: dict = {}
    if "remote_access_session" in value:
        import aws_sdk_device_farm.types.remote_access_session

        out["remoteAccessSession"] = (
            aws_sdk_device_farm.types.remote_access_session.serialize_aws_json_1_1(
                value["remote_access_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRemoteAccessSessionResult:
    out: CreateRemoteAccessSessionResult = {}  # type: ignore[typeddict-item]
    if "remoteAccessSession" in data:
        import aws_sdk_device_farm.types.remote_access_session

        out["remote_access_session"] = (
            aws_sdk_device_farm.types.remote_access_session.deserialize_aws_json_1_1(
                data["remoteAccessSession"]
            )
        )
    return out
