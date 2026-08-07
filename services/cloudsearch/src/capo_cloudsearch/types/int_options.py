"""Generated from Smithy shape ``com.amazonaws.cloudsearch#IntOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.field_name
    import capo_cloudsearch.types.long


class IntOptions(TypedDict, closed=True):
    default_value: NotRequired["capo_cloudsearch.types.long.Long"]
    """A value to use for the field if the field isn't specified for a document. This can be important if you are using the field in an expression and that field is not present in every document."""
    source_field: NotRequired["capo_cloudsearch.types.field_name.FieldName"]
    """<p>The name of the source field to map to the field. </p>"""
    facet_enabled: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether facet information can be returned for the field.</p>"""
    search_enabled: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether the contents of the field are searchable.</p>"""
    return_enabled: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether the contents of the field can be returned in the search results.</p>"""
    sort_enabled: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether the field can be used to sort the search results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IntOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "default_value" in value:
        pairs.append((f"{key_prefix}DefaultValue", str(value["default_value"])))
    if "source_field" in value:
        pairs.append((f"{key_prefix}SourceField", str(value["source_field"])))
    if "facet_enabled" in value:
        pairs.append(
            (f"{key_prefix}FacetEnabled", "true" if value["facet_enabled"] else "false")
        )
    if "search_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}SearchEnabled",
                "true" if value["search_enabled"] else "false",
            )
        )
    if "return_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ReturnEnabled",
                "true" if value["return_enabled"] else "false",
            )
        )
    if "sort_enabled" in value:
        pairs.append(
            (f"{key_prefix}SortEnabled", "true" if value["sort_enabled"] else "false")
        )


def deserialize_query(el: Element) -> IntOptions:
    out: IntOptions = {}  # type: ignore[typeddict-item]
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = int(child_default_value.text or "")
    child_source_field = el.find("SourceField")
    if child_source_field is not None:
        out["source_field"] = str(child_source_field.text or "")
    child_facet_enabled = el.find("FacetEnabled")
    if child_facet_enabled is not None:
        out["facet_enabled"] = (child_facet_enabled.text or "").lower() == "true"
    child_search_enabled = el.find("SearchEnabled")
    if child_search_enabled is not None:
        out["search_enabled"] = (child_search_enabled.text or "").lower() == "true"
    child_return_enabled = el.find("ReturnEnabled")
    if child_return_enabled is not None:
        out["return_enabled"] = (child_return_enabled.text or "").lower() == "true"
    child_sort_enabled = el.find("SortEnabled")
    if child_sort_enabled is not None:
        out["sort_enabled"] = (child_sort_enabled.text or "").lower() == "true"
    return out
