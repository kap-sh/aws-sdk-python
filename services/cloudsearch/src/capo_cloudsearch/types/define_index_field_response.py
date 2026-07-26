"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineIndexFieldResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.index_field_status


class DefineIndexFieldResponse(TypedDict, closed=True):
    index_field: "capo_cloudsearch.types.index_field_status.IndexFieldStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineIndexFieldResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.index_field_status

    capo_cloudsearch.types.index_field_status.serialize_query(
        value["index_field"], pairs, f"{prefix}.IndexField"
    )


def deserialize_query(el: Element) -> DefineIndexFieldResponse:
    out: DefineIndexFieldResponse = {}  # type: ignore[typeddict-item]
    child_index_field = el.find("IndexField")
    if child_index_field is not None:
        import capo_cloudsearch.types.index_field_status

        out["index_field"] = (
            capo_cloudsearch.types.index_field_status.deserialize_query(
                child_index_field
            )
        )
    else:
        raise DeserializationError("DefineIndexFieldResponse.index_field required")
    return out
