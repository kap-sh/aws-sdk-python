"""Generated from Smithy shape ``com.amazonaws.evs#DeleteEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_evs.types.client_token
    import aws_sdk_evs.types.environment_id


class DeleteEnvironmentRequest(TypedDict):
    client_token: NotRequired["aws_sdk_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID associated with the environment to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentRequest:
    out: DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
