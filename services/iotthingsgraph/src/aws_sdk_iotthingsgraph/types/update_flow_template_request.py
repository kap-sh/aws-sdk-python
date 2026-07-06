"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UpdateFlowTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.definition_document
    import aws_sdk_iotthingsgraph.types.urn
    import aws_sdk_iotthingsgraph.types.version


class UpdateFlowTemplateRequest(TypedDict, closed=True):
    id: "aws_sdk_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the workflow to be updated.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>"""
    definition: "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument"
    """<p>The <code>DefinitionDocument</code> that contains the updated workflow definition.</p>"""
    compatible_namespace_version: NotRequired[
        "aws_sdk_iotthingsgraph.types.version.Version"
    ]
    """<p>The version of the user's namespace.</p> <p>If no value is specified, the latest version is used by default. Use the <code>GetFlowTemplateRevisions</code> if you want to find earlier revisions of the flow to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFlowTemplateRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_iotthingsgraph.types.definition_document

    out["definition"] = (
        aws_sdk_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
            value["definition"]
        )
    )
    if "compatible_namespace_version" in value:
        out["compatibleNamespaceVersion"] = value["compatible_namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFlowTemplateRequest:
    out: UpdateFlowTemplateRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateFlowTemplateRequest.id required")
    if "definition" in data:
        import aws_sdk_iotthingsgraph.types.definition_document

        out["definition"] = (
            aws_sdk_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("UpdateFlowTemplateRequest.definition required")
    if "compatibleNamespaceVersion" in data:
        out["compatible_namespace_version"] = data["compatibleNamespaceVersion"]
    return out
