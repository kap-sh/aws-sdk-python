"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CancelLifecycleExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.lifecycle_execution_id


class CancelLifecycleExecutionRequest(TypedDict, closed=True):
    lifecycle_execution_id: (
        "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    )
    """<p>Identifies the specific runtime instance of the image lifecycle to cancel.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelLifecycleExecutionRequest) -> dict:
    out: dict = {}
    out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CancelLifecycleExecutionRequest:
    out: CancelLifecycleExecutionRequest = {}  # type: ignore[typeddict-item]
    if "lifecycleExecutionId" in data:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    else:
        raise DeserializationError(
            "CancelLifecycleExecutionRequest.lifecycle_execution_id required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CancelLifecycleExecutionRequest.client_token required"
        )
    return out
