"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_profile_id


class GetEnvironmentProfileInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this environment profile exists.</p>"""
    identifier: "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
    """<p>The ID of the environment profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentProfileInput:
    out: GetEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
    return out
