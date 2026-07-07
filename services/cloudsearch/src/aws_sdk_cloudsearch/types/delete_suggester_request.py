"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteSuggesterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.standard_name


class DeleteSuggesterRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    suggester_name: "aws_sdk_cloudsearch.types.standard_name.StandardName"
    """<p>Specifies the name of the suggester you want to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSuggesterRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    pairs.append((f"{prefix}.SuggesterName", str(value["suggester_name"])))


def deserialize_query(el: Element) -> DeleteSuggesterRequest:
    out: DeleteSuggesterRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DeleteSuggesterRequest.domain_name required")
    child_suggester_name = el.find("SuggesterName")
    if child_suggester_name is not None:
        out["suggester_name"] = str(child_suggester_name.text or "")
    else:
        raise DeserializationError("DeleteSuggesterRequest.suggester_name required")
    return out
