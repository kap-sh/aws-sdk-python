"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteEnvironmentProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_profile_id


class DeleteEnvironmentProfileInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the environment profile is deleted.</p>"""
    identifier: "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
    """<p>The ID of the environment profile that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentProfileInput:
    out: DeleteEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
    return out
