"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id


class GetDomainInput(TypedDict, closed=True):
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p>The id of the Domain to get</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainInput:
    out: GetDomainInput = {}  # type: ignore[typeddict-item]
    return out
