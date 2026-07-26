"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeleteDomainResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.domain_description


class DeleteDomainResult(TypedDict, closed=True):
    domain: NotRequired["capo_codeartifact.types.domain_description.DomainDescription"]
    """<p> Contains information about the deleted domain after processing the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainResult) -> dict:
    out: dict = {}
    if "domain" in value:
        import capo_codeartifact.types.domain_description

        out["domain"] = capo_codeartifact.types.domain_description.serialize_json(
            value["domain"]
        )
    return out


def deserialize_json(data: dict) -> DeleteDomainResult:
    out: DeleteDomainResult = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        import capo_codeartifact.types.domain_description

        out["domain"] = capo_codeartifact.types.domain_description.deserialize_json(
            data["domain"]
        )
    return out
