"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteSegmentDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class DeleteSegmentDefinitionRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the segment definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSegmentDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSegmentDefinitionRequest:
    out: DeleteSegmentDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
