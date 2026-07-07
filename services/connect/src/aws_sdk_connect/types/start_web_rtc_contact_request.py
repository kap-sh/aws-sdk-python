"""Generated from Smithy shape ``com.amazonaws.connect#StartWebRTCContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.allowed_capabilities
    import aws_sdk_connect.types.attributes
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.contact_references
    import aws_sdk_connect.types.description
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.participant_details


class StartWebRTCContactRequest(TypedDict, closed=True):
    attributes: NotRequired["aws_sdk_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.</p> <p>There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, -, and _ characters.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p> <p>The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.</p>"""
    contact_flow_id: "aws_sdk_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow for the call. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to <b>Routing</b>, <b>Flows</b>. Choose the flow. On the flow page, under the name of the flow, choose <b>Show additional flow information</b>. The ContactFlowId is the last part of the ARN, shown here in bold: </p> <p>arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/<b>846ec553-a005-41c0-8341-xxxxxxxxxxxx</b> </p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    allowed_capabilities: NotRequired[
        "aws_sdk_connect.types.allowed_capabilities.AllowedCapabilities"
    ]
    """<p>Information about the video sharing capabilities of the participants (customer, agent).</p>"""
    participant_details: "aws_sdk_connect.types.participant_details.ParticipantDetails"
    related_contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The unique identifier for an Connect Customer contact. This identifier is related to the contact starting.</p>"""
    references: NotRequired[
        "aws_sdk_connect.types.contact_references.ContactReferences"
    ]
    """<p>A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: <code>URL</code> | <code>NUMBER</code> | <code>STRING</code> | <code>DATE</code> | <code>EMAIL</code>. <code>ATTACHMENT</code> is not a supported reference type during task creation.</p>"""
    description: NotRequired["aws_sdk_connect.types.description.Description"]
    """<p>A description of the task that is shown to an agent in the Contact Control Panel (CCP).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartWebRTCContactRequest) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_connect.types.attributes

        out["Attributes"] = aws_sdk_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ContactFlowId"] = value["contact_flow_id"]
    out["InstanceId"] = value["instance_id"]
    if "allowed_capabilities" in value:
        import aws_sdk_connect.types.allowed_capabilities

        out["AllowedCapabilities"] = (
            aws_sdk_connect.types.allowed_capabilities.serialize_json(
                value["allowed_capabilities"]
            )
        )
    import aws_sdk_connect.types.participant_details

    out["ParticipantDetails"] = (
        aws_sdk_connect.types.participant_details.serialize_json(
            value["participant_details"]
        )
    )
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "references" in value:
        import aws_sdk_connect.types.contact_references

        out["References"] = aws_sdk_connect.types.contact_references.serialize_json(
            value["references"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StartWebRTCContactRequest:
    out: StartWebRTCContactRequest = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_connect.types.attributes

        out["attributes"] = aws_sdk_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("StartWebRTCContactRequest.contact_flow_id required")
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartWebRTCContactRequest.instance_id required")
    if "AllowedCapabilities" in data:
        import aws_sdk_connect.types.allowed_capabilities

        out["allowed_capabilities"] = (
            aws_sdk_connect.types.allowed_capabilities.deserialize_json(
                data["AllowedCapabilities"]
            )
        )
    if "ParticipantDetails" in data:
        import aws_sdk_connect.types.participant_details

        out["participant_details"] = (
            aws_sdk_connect.types.participant_details.deserialize_json(
                data["ParticipantDetails"]
            )
        )
    else:
        raise DeserializationError(
            "StartWebRTCContactRequest.participant_details required"
        )
    if "RelatedContactId" in data:
        out["related_contact_id"] = data["RelatedContactId"]
    if "References" in data:
        import aws_sdk_connect.types.contact_references

        out["references"] = aws_sdk_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
