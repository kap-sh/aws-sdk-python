"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DoubleOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.boolean
    import aws_sdk_cloudsearch.types.double
    import aws_sdk_cloudsearch.types.field_name


class DoubleOptions(TypedDict):
    default_value: NotRequired["aws_sdk_cloudsearch.types.double.Double"]
    """<p>A value to use for the field if the field isn't specified for a document. This can be important if you are using the field in an expression and that field is not present in every document.</p>"""
    source_field: NotRequired["aws_sdk_cloudsearch.types.field_name.FieldName"]
    """<p>The name of the source field to map to the field. </p>"""
    facet_enabled: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>Whether facet information can be returned for the field.</p>"""
    search_enabled: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>Whether the contents of the field are searchable.</p>"""
    return_enabled: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>Whether the contents of the field can be returned in the search results.</p>"""
    sort_enabled: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>Whether the field can be used to sort the search results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DoubleOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "default_value" in value:
        pairs.append((f"{prefix}.DefaultValue", str(value["default_value"])))
    if "source_field" in value:
        pairs.append((f"{prefix}.SourceField", str(value["source_field"])))
    if "facet_enabled" in value:
        pairs.append(
            (f"{prefix}.FacetEnabled", "true" if value["facet_enabled"] else "false")
        )
    if "search_enabled" in value:
        pairs.append(
            (f"{prefix}.SearchEnabled", "true" if value["search_enabled"] else "false")
        )
    if "return_enabled" in value:
        pairs.append(
            (f"{prefix}.ReturnEnabled", "true" if value["return_enabled"] else "false")
        )
    if "sort_enabled" in value:
        pairs.append(
            (f"{prefix}.SortEnabled", "true" if value["sort_enabled"] else "false")
        )


def deserialize_query(el: Element) -> DoubleOptions:
    out: DoubleOptions = {}  # type: ignore[typeddict-item]
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = float(child_default_value.text or "")
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
