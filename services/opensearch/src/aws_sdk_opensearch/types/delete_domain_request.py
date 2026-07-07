"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name


class DeleteDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain you want to permanently delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainRequest:
    out: DeleteDomainRequest = {}  # type: ignore[typeddict-item]
    return out
