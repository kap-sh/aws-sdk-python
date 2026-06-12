"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteIndexFieldRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.dynamic_field_name


class DeleteIndexFieldRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    index_field_name: "aws_sdk_cloudsearch.types.dynamic_field_name.DynamicFieldName"
    """<p>The name of the index field your want to remove from the domain's indexing options.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIndexFieldRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    pairs.append((f"{prefix}.IndexFieldName", str(value["index_field_name"])))


def deserialize_query(el: Element) -> DeleteIndexFieldRequest:
    out: DeleteIndexFieldRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DeleteIndexFieldRequest.domain_name required")
    child_index_field_name = el.find("IndexFieldName")
    if child_index_field_name is not None:
        out["index_field_name"] = str(child_index_field_name.text or "")
    else:
        raise DeserializationError("DeleteIndexFieldRequest.index_field_name required")
    return out
