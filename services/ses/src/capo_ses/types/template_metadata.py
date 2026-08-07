"""Generated from Smithy shape ``com.amazonaws.ses#TemplateMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.template_name
    import capo_ses.types.timestamp


class TemplateMetadata(TypedDict, closed=True):
    name: NotRequired["capo_ses.types.template_name.TemplateName"]
    """<p>The name of the template.</p>"""
    created_timestamp: NotRequired["capo_ses.types.timestamp.Timestamp"]
    """<p>The time and date the template was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "created_timestamp" in value:
        import capo_ses.types.timestamp

        capo_ses.types.timestamp.serialize_query(
            value["created_timestamp"], pairs, f"{key_prefix}CreatedTimestamp"
        )


def deserialize_query(el: Element) -> TemplateMetadata:
    out: TemplateMetadata = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_created_timestamp = el.find("CreatedTimestamp")
    if child_created_timestamp is not None:
        import capo_ses.types.timestamp

        out["created_timestamp"] = capo_ses.types.timestamp.deserialize_query(
            child_created_timestamp
        )
    return out
