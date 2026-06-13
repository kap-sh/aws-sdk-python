"""Generated from Smithy shape ``com.amazonaws.mgn#SsmDocument``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.ssm_document_external_parameters
    import aws_sdk_mgn.types.ssm_document_name
    import aws_sdk_mgn.types.ssm_document_parameters
    import aws_sdk_mgn.types.strictly_positive_integer


class SsmDocument(TypedDict):
    action_name: "aws_sdk_mgn.types.bounded_string.BoundedString"
    """<p>User-friendly name for the AWS Systems Manager Document.</p>"""
    ssm_document_name: "aws_sdk_mgn.types.ssm_document_name.SsmDocumentName"
    """<p>AWS Systems Manager Document name or full ARN.</p>"""
    timeout_seconds: NotRequired[
        "aws_sdk_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>AWS Systems Manager Document timeout seconds.</p>"""
    must_succeed_for_cutover: NotRequired["bool"]
    """<p>If true, Cutover will not be enabled if the document has failed.</p>"""
    parameters: NotRequired[
        "aws_sdk_mgn.types.ssm_document_parameters.SsmDocumentParameters"
    ]
    """<p>AWS Systems Manager Document parameters.</p>"""
    external_parameters: NotRequired[
        "aws_sdk_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
    ]
    """<p>AWS Systems Manager Document external parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsmDocument) -> dict:
    out: dict = {}
    out["actionName"] = value["action_name"]
    out["ssmDocumentName"] = value["ssm_document_name"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "must_succeed_for_cutover" in value:
        out["mustSucceedForCutover"] = value["must_succeed_for_cutover"]
    if "parameters" in value:
        import aws_sdk_mgn.types.ssm_document_parameters

        out["parameters"] = aws_sdk_mgn.types.ssm_document_parameters.serialize_json(
            value["parameters"]
        )
    if "external_parameters" in value:
        import aws_sdk_mgn.types.ssm_document_external_parameters

        out["externalParameters"] = (
            aws_sdk_mgn.types.ssm_document_external_parameters.serialize_json(
                value["external_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SsmDocument:
    out: SsmDocument = {}  # type: ignore[typeddict-item]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    else:
        raise DeserializationError("SsmDocument.action_name required")
    if "ssmDocumentName" in data:
        out["ssm_document_name"] = data["ssmDocumentName"]
    else:
        raise DeserializationError("SsmDocument.ssm_document_name required")
    if "timeoutSeconds" in data:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if "mustSucceedForCutover" in data:
        out["must_succeed_for_cutover"] = data["mustSucceedForCutover"]
    if "parameters" in data:
        import aws_sdk_mgn.types.ssm_document_parameters

        out["parameters"] = aws_sdk_mgn.types.ssm_document_parameters.deserialize_json(
            data["parameters"]
        )
    if "externalParameters" in data:
        import aws_sdk_mgn.types.ssm_document_external_parameters

        out["external_parameters"] = (
            aws_sdk_mgn.types.ssm_document_external_parameters.deserialize_json(
                data["externalParameters"]
            )
        )
    return out
