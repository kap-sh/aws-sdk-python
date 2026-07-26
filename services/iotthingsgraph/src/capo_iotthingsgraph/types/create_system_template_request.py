"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#CreateSystemTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.definition_document
    import capo_iotthingsgraph.types.version


class CreateSystemTemplateRequest(TypedDict, closed=True):
    definition: "capo_iotthingsgraph.types.definition_document.DefinitionDocument"
    """<p>The <code>DefinitionDocument</code> used to create the system.</p>"""
    compatible_namespace_version: NotRequired[
        "capo_iotthingsgraph.types.version.Version"
    ]
    """<p>The namespace version in which the system is to be created.</p> <p>If no value is specified, the latest version is used by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSystemTemplateRequest) -> dict:
    out: dict = {}
    import capo_iotthingsgraph.types.definition_document

    out["definition"] = (
        capo_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
            value["definition"]
        )
    )
    if "compatible_namespace_version" in value:
        out["compatibleNamespaceVersion"] = value["compatible_namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSystemTemplateRequest:
    out: CreateSystemTemplateRequest = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        import capo_iotthingsgraph.types.definition_document

        out["definition"] = (
            capo_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("CreateSystemTemplateRequest.definition required")
    if "compatibleNamespaceVersion" in data:
        out["compatible_namespace_version"] = data["compatibleNamespaceVersion"]
    return out
