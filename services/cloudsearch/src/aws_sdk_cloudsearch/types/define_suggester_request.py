"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineSuggesterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.suggester


class DefineSuggesterRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    suggester: "aws_sdk_cloudsearch.types.suggester.Suggester"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineSuggesterRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    import aws_sdk_cloudsearch.types.suggester

    aws_sdk_cloudsearch.types.suggester.serialize_query(
        value["suggester"], pairs, f"{prefix}.Suggester"
    )


def deserialize_query(el: Element) -> DefineSuggesterRequest:
    out: DefineSuggesterRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DefineSuggesterRequest.domain_name required")
    child_suggester = el.find("Suggester")
    if child_suggester is not None:
        import aws_sdk_cloudsearch.types.suggester

        out["suggester"] = aws_sdk_cloudsearch.types.suggester.deserialize_query(
            child_suggester
        )
    else:
        raise DeserializationError("DefineSuggesterRequest.suggester required")
    return out
