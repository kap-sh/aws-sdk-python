"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowTemplateDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.definition_document
    import capo_iotthingsgraph.types.flow_template_summary
    import capo_iotthingsgraph.types.version


class FlowTemplateDescription(TypedDict, closed=True):
    summary: NotRequired[
        "capo_iotthingsgraph.types.flow_template_summary.FlowTemplateSummary"
    ]
    """<p>An object that contains summary information about a workflow.</p>"""
    definition: NotRequired[
        "capo_iotthingsgraph.types.definition_document.DefinitionDocument"
    ]
    """<p>A workflow's definition document.</p>"""
    validated_namespace_version: NotRequired[
        "capo_iotthingsgraph.types.version.Version"
    ]
    """<p>The version of the user's namespace against which the workflow was validated. Use this value in your system instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowTemplateDescription) -> dict:
    out: dict = {}
    if "summary" in value:
        import capo_iotthingsgraph.types.flow_template_summary

        out["summary"] = (
            capo_iotthingsgraph.types.flow_template_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    if "definition" in value:
        import capo_iotthingsgraph.types.definition_document

        out["definition"] = (
            capo_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
                value["definition"]
            )
        )
    if "validated_namespace_version" in value:
        out["validatedNamespaceVersion"] = value["validated_namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlowTemplateDescription:
    out: FlowTemplateDescription = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import capo_iotthingsgraph.types.flow_template_summary

        out["summary"] = (
            capo_iotthingsgraph.types.flow_template_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    if "definition" in data:
        import capo_iotthingsgraph.types.definition_document

        out["definition"] = (
            capo_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["definition"]
            )
        )
    if "validatedNamespaceVersion" in data:
        out["validated_namespace_version"] = data["validatedNamespaceVersion"]
    return out
