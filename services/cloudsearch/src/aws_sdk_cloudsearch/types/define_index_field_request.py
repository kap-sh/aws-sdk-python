"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineIndexFieldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.index_field


class DefineIndexFieldRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    index_field: "aws_sdk_cloudsearch.types.index_field.IndexField"
    """<p>The index field and field options you want to configure. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineIndexFieldRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    import aws_sdk_cloudsearch.types.index_field

    aws_sdk_cloudsearch.types.index_field.serialize_query(
        value["index_field"], pairs, f"{prefix}.IndexField"
    )


def deserialize_query(el: Element) -> DefineIndexFieldRequest:
    out: DefineIndexFieldRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DefineIndexFieldRequest.domain_name required")
    child_index_field = el.find("IndexField")
    if child_index_field is not None:
        import aws_sdk_cloudsearch.types.index_field

        out["index_field"] = aws_sdk_cloudsearch.types.index_field.deserialize_query(
            child_index_field
        )
    else:
        raise DeserializationError("DefineIndexFieldRequest.index_field required")
    return out
