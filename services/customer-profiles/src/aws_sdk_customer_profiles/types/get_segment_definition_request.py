"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class GetSegmentDefinitionRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the segment definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSegmentDefinitionRequest:
    out: GetSegmentDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
