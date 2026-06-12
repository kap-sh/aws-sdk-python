"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteSegmentDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class DeleteSegmentDefinitionRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the segment definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSegmentDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSegmentDefinitionRequest:
    out: DeleteSegmentDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
