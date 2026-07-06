"""Generated from Smithy shape ``com.amazonaws.cloudsearch#IndexDocumentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.field_name_list


class IndexDocumentsResponse(TypedDict, closed=True):
    field_names: NotRequired["aws_sdk_cloudsearch.types.field_name_list.FieldNameList"]
    """<p>The names of the fields that are currently being indexed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IndexDocumentsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "field_names" in value:
        import aws_sdk_cloudsearch.types.field_name_list

        aws_sdk_cloudsearch.types.field_name_list.serialize_query(
            value["field_names"], pairs, f"{prefix}.FieldNames"
        )


def deserialize_query(el: Element) -> IndexDocumentsResponse:
    out: IndexDocumentsResponse = {}  # type: ignore[typeddict-item]
    child_field_names = el.find("FieldNames")
    if child_field_names is not None:
        import aws_sdk_cloudsearch.types.field_name_list

        out["field_names"] = (
            aws_sdk_cloudsearch.types.field_name_list.deserialize_query(
                child_field_names
            )
        )
    return out
