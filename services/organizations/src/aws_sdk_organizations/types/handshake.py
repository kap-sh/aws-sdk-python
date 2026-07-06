"""Generated from Smithy shape ``com.amazonaws.organizations#Handshake``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.action_type
    import aws_sdk_organizations.types.handshake_arn
    import aws_sdk_organizations.types.handshake_id
    import aws_sdk_organizations.types.handshake_parties
    import aws_sdk_organizations.types.handshake_resources
    import aws_sdk_organizations.types.handshake_state
    import aws_sdk_organizations.types.timestamp


class Handshake(TypedDict, closed=True):
    id: NotRequired["aws_sdk_organizations.types.handshake_id.HandshakeId"]
    r"""<p>ID for the handshake.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for handshake ID string requires \"h-\" followed by from 8 to 32 lowercase letters or digits.</p>"""
    arn: NotRequired["aws_sdk_organizations.types.handshake_arn.HandshakeArn"]
    r"""<p>Amazon Resource Name (ARN) for the handshake.</p> <p>For more information about ARNs in Organizations, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies\">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    parties: NotRequired[
        "aws_sdk_organizations.types.handshake_parties.HandshakeParties"
    ]
    """<p>An array of <code>HandshakeParty</code> objects. Contains details for participant in a handshake.</p>"""
    state: NotRequired["aws_sdk_organizations.types.handshake_state.HandshakeState"]
    """<p>Current state for the handshake.</p> <ul> <li> <p> <b>REQUESTED</b>: Handshake awaiting a response from the recipient.</p> </li> <li> <p> <b>OPEN</b>: Handshake sent to multiple recipients and all recipients have responded. The sender can now complete the handshake action.</p> </li> <li> <p> <b>CANCELED</b>: Handshake canceled by the sender.</p> </li> <li> <p> <b>ACCEPTED</b>: Handshake accepted by the recipient.</p> </li> <li> <p> <b>DECLINED</b>: Handshake declined by the recipient.</p> </li> <li> <p> <b>EXPIRED</b>: Handshake has expired.</p> </li> </ul>"""
    requested_timestamp: NotRequired["aws_sdk_organizations.types.timestamp.Timestamp"]
    """<p>Timestamp when the handshake request was made.</p>"""
    expiration_timestamp: NotRequired["aws_sdk_organizations.types.timestamp.Timestamp"]
    """<p>Timestamp when the handshake expires.</p>"""
    action: NotRequired["aws_sdk_organizations.types.action_type.ActionType"]
    """<p>The type of handshake:</p> <ul> <li> <p> <b>INVITE</b>: Handshake sent to a standalone account requesting that it to join the sender's organization.</p> </li> <li> <p> <b>ENABLE_ALL_FEATURES</b>: Handshake sent to invited member accounts to enable all features for the organization.</p> </li> <li> <p> <b>APPROVE_ALL_FEATURES</b>: Handshake sent to the management account when all invited member accounts have approved to enable all features.</p> </li> <li> <p> <b>TRANSFER_RESPONSIBILITY</b>: Handshake sent to another organization's management account requesting that it designate the sender with the specified responsibilities for recipient's organization.</p> </li> </ul>"""
    resources: NotRequired[
        "aws_sdk_organizations.types.handshake_resources.HandshakeResources"
    ]
    """<p>An array of <code>HandshakeResource</code> objects. When needed, contains additional details for a handshake. For example, the email address for the sender.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Handshake) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "parties" in value:
        import aws_sdk_organizations.types.handshake_parties

        out["Parties"] = (
            aws_sdk_organizations.types.handshake_parties.serialize_aws_json_1_1(
                value["parties"]
            )
        )
    if "state" in value:
        import aws_sdk_organizations.types.handshake_state

        out["State"] = (
            aws_sdk_organizations.types.handshake_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "requested_timestamp" in value:
        import aws_sdk_organizations.types.timestamp

        out["RequestedTimestamp"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["requested_timestamp"]
            )
        )
    if "expiration_timestamp" in value:
        import aws_sdk_organizations.types.timestamp

        out["ExpirationTimestamp"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["expiration_timestamp"]
            )
        )
    if "action" in value:
        import aws_sdk_organizations.types.action_type

        out["Action"] = aws_sdk_organizations.types.action_type.serialize_aws_json_1_1(
            value["action"]
        )
    if "resources" in value:
        import aws_sdk_organizations.types.handshake_resources

        out["Resources"] = (
            aws_sdk_organizations.types.handshake_resources.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Handshake:
    out: Handshake = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Parties" in data:
        import aws_sdk_organizations.types.handshake_parties

        out["parties"] = (
            aws_sdk_organizations.types.handshake_parties.deserialize_aws_json_1_1(
                data["Parties"]
            )
        )
    if "State" in data:
        import aws_sdk_organizations.types.handshake_state

        out["state"] = (
            aws_sdk_organizations.types.handshake_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "RequestedTimestamp" in data:
        import aws_sdk_organizations.types.timestamp

        out["requested_timestamp"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["RequestedTimestamp"]
            )
        )
    if "ExpirationTimestamp" in data:
        import aws_sdk_organizations.types.timestamp

        out["expiration_timestamp"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTimestamp"]
            )
        )
    if "Action" in data:
        import aws_sdk_organizations.types.action_type

        out["action"] = (
            aws_sdk_organizations.types.action_type.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    if "Resources" in data:
        import aws_sdk_organizations.types.handshake_resources

        out["resources"] = (
            aws_sdk_organizations.types.handshake_resources.deserialize_aws_json_1_1(
                data["Resources"]
            )
        )
    return out
