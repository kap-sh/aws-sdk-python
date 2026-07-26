"""Generated from Smithy shape ``com.amazonaws.mgn#SourceServerActionDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.action_category
    import capo_mgn.types.action_description
    import capo_mgn.types.action_id
    import capo_mgn.types.action_name
    import capo_mgn.types.bounded_string
    import capo_mgn.types.document_version
    import capo_mgn.types.order_type
    import capo_mgn.types.ssm_document_external_parameters
    import capo_mgn.types.ssm_document_parameters
    import capo_mgn.types.strictly_positive_integer


class SourceServerActionDocument(TypedDict, closed=True):
    action_id: NotRequired["capo_mgn.types.action_id.ActionID"]
    """<p>Source server post migration custom action ID.</p>"""
    action_name: NotRequired["capo_mgn.types.action_name.ActionName"]
    """<p>Source server post migration custom action name.</p>"""
    document_identifier: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Source server post migration custom action document identifier.</p>"""
    order: NotRequired["capo_mgn.types.order_type.OrderType"]
    """<p>Source server post migration custom action order.</p>"""
    document_version: NotRequired["capo_mgn.types.document_version.DocumentVersion"]
    """<p>Source server post migration custom action document version.</p>"""
    active: NotRequired["bool"]
    """<p>Source server post migration custom action active status.</p>"""
    timeout_seconds: NotRequired[
        "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Source server post migration custom action timeout in seconds.</p>"""
    must_succeed_for_cutover: NotRequired["bool"]
    """<p>Source server post migration custom action must succeed for cutover.</p>"""
    parameters: NotRequired[
        "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
    ]
    """<p>Source server post migration custom action parameters.</p>"""
    external_parameters: NotRequired[
        "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
    ]
    """<p>Source server post migration custom action external parameters.</p>"""
    description: NotRequired["capo_mgn.types.action_description.ActionDescription"]
    """<p>Source server post migration custom action description.</p>"""
    category: NotRequired["capo_mgn.types.action_category.ActionCategory"]
    """<p>Source server post migration custom action category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceServerActionDocument) -> dict:
    out: dict = {}
    if "action_id" in value:
        out["actionID"] = value["action_id"]
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "document_identifier" in value:
        out["documentIdentifier"] = value["document_identifier"]
    if "order" in value:
        out["order"] = value["order"]
    if "document_version" in value:
        out["documentVersion"] = value["document_version"]
    if "active" in value:
        out["active"] = value["active"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "must_succeed_for_cutover" in value:
        out["mustSucceedForCutover"] = value["must_succeed_for_cutover"]
    if "parameters" in value:
        import capo_mgn.types.ssm_document_parameters

        out["parameters"] = capo_mgn.types.ssm_document_parameters.serialize_json(
            value["parameters"]
        )
    if "external_parameters" in value:
        import capo_mgn.types.ssm_document_external_parameters

        out["externalParameters"] = (
            capo_mgn.types.ssm_document_external_parameters.serialize_json(
                value["external_parameters"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    return out


def deserialize_json(data: dict) -> SourceServerActionDocument:
    out: SourceServerActionDocument = {}  # type: ignore[typeddict-item]
    if "actionID" in data:
        out["action_id"] = data["actionID"]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    if "documentIdentifier" in data:
        out["document_identifier"] = data["documentIdentifier"]
    if "order" in data:
        out["order"] = data["order"]
    if "documentVersion" in data:
        out["document_version"] = data["documentVersion"]
    if "active" in data:
        out["active"] = data["active"]
    if "timeoutSeconds" in data:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if "mustSucceedForCutover" in data:
        out["must_succeed_for_cutover"] = data["mustSucceedForCutover"]
    if "parameters" in data:
        import capo_mgn.types.ssm_document_parameters

        out["parameters"] = capo_mgn.types.ssm_document_parameters.deserialize_json(
            data["parameters"]
        )
    if "externalParameters" in data:
        import capo_mgn.types.ssm_document_external_parameters

        out["external_parameters"] = (
            capo_mgn.types.ssm_document_external_parameters.deserialize_json(
                data["externalParameters"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "category" in data:
        out["category"] = data["category"]
    return out
