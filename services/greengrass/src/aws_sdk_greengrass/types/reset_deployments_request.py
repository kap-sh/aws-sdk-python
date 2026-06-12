"""Generated from Smithy shape ``com.amazonaws.greengrass#ResetDeploymentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__boolean
    import aws_sdk_greengrass.types.__string


class ResetDeploymentsRequest(TypedDict):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    force: NotRequired["aws_sdk_greengrass.types.__boolean.__boolean"]
    """If true, performs a best-effort only core reset."""
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: ResetDeploymentsRequest) -> dict:
    out: dict = {}
    if "force" in value:
        out["Force"] = value["force"]
    return out


def deserialize_json(data: dict) -> ResetDeploymentsRequest:
    out: ResetDeploymentsRequest = {}  # type: ignore[typeddict-item]
    if "Force" in data:
        out["force"] = data["Force"]
    return out
