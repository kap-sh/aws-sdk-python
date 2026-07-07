"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteIndexFieldResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.index_field_status


class DeleteIndexFieldResponse(TypedDict, closed=True):
    index_field: "aws_sdk_cloudsearch.types.index_field_status.IndexFieldStatus"
    """<p>The status of the index field being deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIndexFieldResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.index_field_status

    aws_sdk_cloudsearch.types.index_field_status.serialize_query(
        value["index_field"], pairs, f"{prefix}.IndexField"
    )


def deserialize_query(el: Element) -> DeleteIndexFieldResponse:
    out: DeleteIndexFieldResponse = {}  # type: ignore[typeddict-item]
    child_index_field = el.find("IndexField")
    if child_index_field is not None:
        import aws_sdk_cloudsearch.types.index_field_status

        out["index_field"] = (
            aws_sdk_cloudsearch.types.index_field_status.deserialize_query(
                child_index_field
            )
        )
    else:
        raise DeserializationError("DeleteIndexFieldResponse.index_field required")
    return out
