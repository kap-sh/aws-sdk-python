"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseEventConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id


class GetCaseEventConfigurationRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseEventConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCaseEventConfigurationRequest:
    out: GetCaseEventConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
