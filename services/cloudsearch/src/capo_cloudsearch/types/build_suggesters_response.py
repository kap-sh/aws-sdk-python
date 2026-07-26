"""Generated from Smithy shape ``com.amazonaws.cloudsearch#BuildSuggestersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.field_name_list


class BuildSuggestersResponse(TypedDict, closed=True):
    field_names: NotRequired["capo_cloudsearch.types.field_name_list.FieldNameList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: BuildSuggestersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "field_names" in value:
        import capo_cloudsearch.types.field_name_list

        capo_cloudsearch.types.field_name_list.serialize_query(
            value["field_names"], pairs, f"{prefix}.FieldNames"
        )


def deserialize_query(el: Element) -> BuildSuggestersResponse:
    out: BuildSuggestersResponse = {}  # type: ignore[typeddict-item]
    child_field_names = el.find("FieldNames")
    if child_field_names is not None:
        import capo_cloudsearch.types.field_name_list

        out["field_names"] = capo_cloudsearch.types.field_name_list.deserialize_query(
            child_field_names
        )
    return out
