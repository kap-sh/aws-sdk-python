"""Generated from Smithy shape ``com.amazonaws.medialive#StartDeleteMonitorDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class StartDeleteMonitorDeploymentRequest(TypedDict):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """A signal map's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: StartDeleteMonitorDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartDeleteMonitorDeploymentRequest:
    out: StartDeleteMonitorDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
