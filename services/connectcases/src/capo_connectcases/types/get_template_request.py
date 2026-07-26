"""Generated from Smithy shape ``com.amazonaws.connectcases#GetTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.template_id


class GetTemplateRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    template_id: "capo_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTemplateRequest:
    out: GetTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
