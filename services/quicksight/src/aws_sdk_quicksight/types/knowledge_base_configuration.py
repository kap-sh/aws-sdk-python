"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.kb_template_configuration


class KnowledgeBaseConfiguration(TypedDict, closed=True):
    template_configuration: NotRequired[
        "aws_sdk_quicksight.types.kb_template_configuration.KbTemplateConfiguration"
    ]
    """<p>The template configuration for the knowledge base.</p>"""
    event_enabled: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>Indicates whether event notifications are enabled for the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    if "template_configuration" in value:
        import aws_sdk_quicksight.types.kb_template_configuration

        out["templateConfiguration"] = (
            aws_sdk_quicksight.types.kb_template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    if "event_enabled" in value:
        out["eventEnabled"] = value["event_enabled"]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseConfiguration:
    out: KnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if "templateConfiguration" in data:
        import aws_sdk_quicksight.types.kb_template_configuration

        out["template_configuration"] = (
            aws_sdk_quicksight.types.kb_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    if "eventEnabled" in data:
        out["event_enabled"] = data["eventEnabled"]
    return out
