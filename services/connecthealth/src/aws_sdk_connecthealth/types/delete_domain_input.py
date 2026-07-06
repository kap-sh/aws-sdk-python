"""Generated from Smithy shape ``com.amazonaws.connecthealth#DeleteDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id


class DeleteDomainInput(TypedDict, closed=True):
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p>The id of the Domain to delete</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainInput:
    out: DeleteDomainInput = {}  # type: ignore[typeddict-item]
    return out
