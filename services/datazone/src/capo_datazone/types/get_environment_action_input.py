"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id


class GetEnvironmentActionInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the <code>GetEnvironmentAction</code> API is invoked. </p>"""
    environment_identifier: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The environment ID of the environment action.</p>"""
    identifier: "str"
    """<p>The ID of the environment action</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentActionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentActionInput:
    out: GetEnvironmentActionInput = {}  # type: ignore[typeddict-item]
    return out
