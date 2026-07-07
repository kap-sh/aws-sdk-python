"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemTemplateDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.definition_document
    import aws_sdk_iotthingsgraph.types.system_template_summary
    import aws_sdk_iotthingsgraph.types.version


class SystemTemplateDescription(TypedDict, closed=True):
    summary: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_template_summary.SystemTemplateSummary"
    ]
    """<p>An object that contains summary information about a system.</p>"""
    definition: NotRequired[
        "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument"
    ]
    """<p>The definition document of a system.</p>"""
    validated_namespace_version: NotRequired[
        "aws_sdk_iotthingsgraph.types.version.Version"
    ]
    """<p>The namespace version against which the system was validated. Use this value in your system instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTemplateDescription) -> dict:
    out: dict = {}
    if "summary" in value:
        import aws_sdk_iotthingsgraph.types.system_template_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_template_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    if "definition" in value:
        import aws_sdk_iotthingsgraph.types.definition_document

        out["definition"] = (
            aws_sdk_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
                value["definition"]
            )
        )
    if "validated_namespace_version" in value:
        out["validatedNamespaceVersion"] = value["validated_namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SystemTemplateDescription:
    out: SystemTemplateDescription = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import aws_sdk_iotthingsgraph.types.system_template_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_template_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    if "definition" in data:
        import aws_sdk_iotthingsgraph.types.definition_document

        out["definition"] = (
            aws_sdk_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["definition"]
            )
        )
    if "validatedNamespaceVersion" in data:
        out["validated_namespace_version"] = data["validatedNamespaceVersion"]
    return out
