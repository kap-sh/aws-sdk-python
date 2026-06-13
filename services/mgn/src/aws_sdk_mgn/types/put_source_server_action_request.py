"""Generated from Smithy shape ``com.amazonaws.mgn#PutSourceServerActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.action_category
    import aws_sdk_mgn.types.action_description
    import aws_sdk_mgn.types.action_id
    import aws_sdk_mgn.types.action_name
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.document_version
    import aws_sdk_mgn.types.order_type
    import aws_sdk_mgn.types.source_server_id
    import aws_sdk_mgn.types.ssm_document_external_parameters
    import aws_sdk_mgn.types.ssm_document_parameters
    import aws_sdk_mgn.types.strictly_positive_integer


class PutSourceServerActionRequest(TypedDict):
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>Source server ID.</p>"""
    action_name: "aws_sdk_mgn.types.action_name.ActionName"
    """<p>Source server post migration custom action name.</p>"""
    document_identifier: "aws_sdk_mgn.types.bounded_string.BoundedString"
    """<p>Source server post migration custom action document identifier.</p>"""
    order: "aws_sdk_mgn.types.order_type.OrderType"
    """<p>Source server post migration custom action order.</p>"""
    action_id: "aws_sdk_mgn.types.action_id.ActionID"
    """<p>Source server post migration custom action ID.</p>"""
    document_version: NotRequired["aws_sdk_mgn.types.document_version.DocumentVersion"]
    """<p>Source server post migration custom action document version.</p>"""
    active: NotRequired["bool"]
    """<p>Source server post migration custom action active status.</p>"""
    timeout_seconds: NotRequired[
        "aws_sdk_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Source server post migration custom action timeout in seconds.</p>"""
    must_succeed_for_cutover: NotRequired["bool"]
    """<p>Source server post migration custom action must succeed for cutover.</p>"""
    parameters: NotRequired[
        "aws_sdk_mgn.types.ssm_document_parameters.SsmDocumentParameters"
    ]
    """<p>Source server post migration custom action parameters.</p>"""
    external_parameters: NotRequired[
        "aws_sdk_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
    ]
    """<p>Source server post migration custom action external parameters.</p>"""
    description: NotRequired["aws_sdk_mgn.types.action_description.ActionDescription"]
    """<p>Source server post migration custom action description.</p>"""
    category: NotRequired["aws_sdk_mgn.types.action_category.ActionCategory"]
    """<p>Source server post migration custom action category.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Source server post migration custom account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSourceServerActionRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    out["actionName"] = value["action_name"]
    out["documentIdentifier"] = value["document_identifier"]
    out["order"] = value["order"]
    out["actionID"] = value["action_id"]
    if "document_version" in value:
        out["documentVersion"] = value["document_version"]
    if "active" in value:
        out["active"] = value["active"]
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
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> PutSourceServerActionRequest:
    out: PutSourceServerActionRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "PutSourceServerActionRequest.source_server_id required"
        )
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    else:
        raise DeserializationError("PutSourceServerActionRequest.action_name required")
    if "documentIdentifier" in data:
        out["document_identifier"] = data["documentIdentifier"]
    else:
        raise DeserializationError(
            "PutSourceServerActionRequest.document_identifier required"
        )
    if "order" in data:
        out["order"] = data["order"]
    else:
        raise DeserializationError("PutSourceServerActionRequest.order required")
    if "actionID" in data:
        out["action_id"] = data["actionID"]
    else:
        raise DeserializationError("PutSourceServerActionRequest.action_id required")
    if "documentVersion" in data:
        out["document_version"] = data["documentVersion"]
    if "active" in data:
        out["active"] = data["active"]
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
    if "description" in data:
        out["description"] = data["description"]
    if "category" in data:
        out["category"] = data["category"]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
