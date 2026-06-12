"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribeDomainResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.domain_description


class DescribeDomainResult(TypedDict):
    domain: NotRequired[
        "aws_sdk_codeartifact.types.domain_description.DomainDescription"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainResult) -> dict:
    out: dict = {}
    if "domain" in value:
        import aws_sdk_codeartifact.types.domain_description

        out["domain"] = aws_sdk_codeartifact.types.domain_description.serialize_json(
            value["domain"]
        )
    return out


def deserialize_json(data: dict) -> DescribeDomainResult:
    out: DescribeDomainResult = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        import aws_sdk_codeartifact.types.domain_description

        out["domain"] = aws_sdk_codeartifact.types.domain_description.deserialize_json(
            data["domain"]
        )
    return out
