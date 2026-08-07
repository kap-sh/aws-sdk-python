"""Generated from Smithy shape ``com.amazonaws.cloudsearch#TextArrayOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.field_name_comma_list
    import capo_cloudsearch.types.field_value
    import capo_cloudsearch.types.word


class TextArrayOptions(TypedDict, closed=True):
    default_value: NotRequired["capo_cloudsearch.types.field_value.FieldValue"]
    """A value to use for the field if the field isn't specified for a document."""
    source_fields: NotRequired[
        "capo_cloudsearch.types.field_name_comma_list.FieldNameCommaList"
    ]
    """<p>A list of source fields to map to the field. </p>"""
    return_enabled: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether the contents of the field can be returned in the search results.</p>"""
    highlight_enabled: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether highlights can be returned for the field.</p>"""
    analysis_scheme: NotRequired["capo_cloudsearch.types.word.Word"]
    """<p>The name of an analysis scheme for a <code>text-array</code> field.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TextArrayOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "default_value" in value:
        pairs.append((f"{key_prefix}DefaultValue", str(value["default_value"])))
    if "source_fields" in value:
        pairs.append((f"{key_prefix}SourceFields", str(value["source_fields"])))
    if "return_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ReturnEnabled",
                "true" if value["return_enabled"] else "false",
            )
        )
    if "highlight_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}HighlightEnabled",
                "true" if value["highlight_enabled"] else "false",
            )
        )
    if "analysis_scheme" in value:
        pairs.append((f"{key_prefix}AnalysisScheme", str(value["analysis_scheme"])))


def deserialize_query(el: Element) -> TextArrayOptions:
    out: TextArrayOptions = {}  # type: ignore[typeddict-item]
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_source_fields = el.find("SourceFields")
    if child_source_fields is not None:
        out["source_fields"] = str(child_source_fields.text or "")
    child_return_enabled = el.find("ReturnEnabled")
    if child_return_enabled is not None:
        out["return_enabled"] = (child_return_enabled.text or "").lower() == "true"
    child_highlight_enabled = el.find("HighlightEnabled")
    if child_highlight_enabled is not None:
        out["highlight_enabled"] = (
            child_highlight_enabled.text or ""
        ).lower() == "true"
    child_analysis_scheme = el.find("AnalysisScheme")
    if child_analysis_scheme is not None:
        out["analysis_scheme"] = str(child_analysis_scheme.text or "")
    return out
