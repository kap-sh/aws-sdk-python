"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_status


class CreateDomainResponse(TypedDict):
    domain_status: NotRequired["aws_sdk_opensearch.types.domain_status.DomainStatus"]
    """<p>The status of the newly created domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainResponse) -> dict:
    out: dict = {}
    if "domain_status" in value:
        import aws_sdk_opensearch.types.domain_status

        out["DomainStatus"] = aws_sdk_opensearch.types.domain_status.serialize_json(
            value["domain_status"]
        )
    return out


def deserialize_json(data: dict) -> CreateDomainResponse:
    out: CreateDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainStatus" in data:
        import aws_sdk_opensearch.types.domain_status

        out["domain_status"] = aws_sdk_opensearch.types.domain_status.deserialize_json(
            data["DomainStatus"]
        )
    return out
