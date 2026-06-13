"""Generated from Smithy shape ``com.amazonaws.evs#DeleteEnvironmentHostRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.client_token
    import aws_sdk_evs.types.environment_id
    import aws_sdk_evs.types.host_name


class DeleteEnvironmentHostRequest(TypedDict):
    client_token: NotRequired["aws_sdk_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the host's environment.</p>"""
    host_name: "aws_sdk_evs.types.host_name.HostName"
    """<p>The DNS hostname associated with the host to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentHostRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["environmentId"] = value["environment_id"]
    out["hostName"] = value["host_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentHostRequest:
    out: DeleteEnvironmentHostRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "DeleteEnvironmentHostRequest.environment_id required"
        )
    if "hostName" in data:
        out["host_name"] = data["hostName"]
    else:
        raise DeserializationError("DeleteEnvironmentHostRequest.host_name required")
    return out
