"""Generated from Smithy shape ``com.amazonaws.connectcases#GetDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id


class GetDomainRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainRequest:
    out: GetDomainRequest = {}  # type: ignore[typeddict-item]
    return out
