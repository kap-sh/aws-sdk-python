"""Generated from Smithy shape ``com.amazonaws.connectcases#DeleteDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id


class DeleteDomainRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainRequest:
    out: DeleteDomainRequest = {}  # type: ignore[typeddict-item]
    return out
