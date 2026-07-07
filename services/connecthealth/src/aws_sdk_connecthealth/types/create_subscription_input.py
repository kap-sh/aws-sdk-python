"""Generated from Smithy shape ``com.amazonaws.connecthealth#CreateSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id


class CreateSubscriptionInput(TypedDict, closed=True):
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateSubscriptionInput:
    out: CreateSubscriptionInput = {}  # type: ignore[typeddict-item]
    return out
