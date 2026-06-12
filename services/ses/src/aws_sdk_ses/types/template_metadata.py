"""Generated from Smithy shape ``com.amazonaws.ses#TemplateMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.template_name
    import aws_sdk_ses.types.timestamp


class TemplateMetadata(TypedDict):
    name: NotRequired["aws_sdk_ses.types.template_name.TemplateName"]
    """<p>The name of the template.</p>"""
    created_timestamp: NotRequired["aws_sdk_ses.types.timestamp.Timestamp"]
    """<p>The time and date the template was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "created_timestamp" in value:
        import aws_sdk_ses.types.timestamp

        aws_sdk_ses.types.timestamp.serialize_query(
            value["created_timestamp"], pairs, f"{prefix}.CreatedTimestamp"
        )


def deserialize_query(el: Element) -> TemplateMetadata:
    out: TemplateMetadata = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_created_timestamp = el.find("CreatedTimestamp")
    if child_created_timestamp is not None:
        import aws_sdk_ses.types.timestamp

        out["created_timestamp"] = aws_sdk_ses.types.timestamp.deserialize_query(
            child_created_timestamp
        )
    return out
