"""Generated from Smithy shape ``com.amazonaws.datazone#StopNotebookRunInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.notebook_run_id


class StopNotebookRunInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is stopped.</p>"""
    identifier: "capo_datazone.types.notebook_run_id.NotebookRunId"
    """<p>The identifier of the notebook run to stop.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopNotebookRunInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StopNotebookRunInput:
    out: StopNotebookRunInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
