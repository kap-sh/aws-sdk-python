"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetProfileObjectTypeTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class GetProfileObjectTypeTemplateRequest(TypedDict):
    template_id: "aws_sdk_customer_profiles.types.name.name"
    """<p>A unique identifier for the object template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileObjectTypeTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileObjectTypeTemplateRequest:
    out: GetProfileObjectTypeTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
