"""Generated from Smithy shape ``com.amazonaws.codeartifact#CreateDomainResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.domain_description


class CreateDomainResult(TypedDict):
    domain: NotRequired[
        "aws_sdk_codeartifact.types.domain_description.DomainDescription"
    ]
    """<p> Contains information about the created domain after processing the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainResult) -> dict:
    out: dict = {}
    if "domain" in value:
        import aws_sdk_codeartifact.types.domain_description

        out["domain"] = aws_sdk_codeartifact.types.domain_description.serialize_json(
            value["domain"]
        )
    return out


def deserialize_json(data: dict) -> CreateDomainResult:
    out: CreateDomainResult = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        import aws_sdk_codeartifact.types.domain_description

        out["domain"] = aws_sdk_codeartifact.types.domain_description.deserialize_json(
            data["domain"]
        )
    return out
