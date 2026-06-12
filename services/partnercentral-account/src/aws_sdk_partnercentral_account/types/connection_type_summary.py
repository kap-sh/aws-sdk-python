"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.connection_type_status
    import aws_sdk_partnercentral_account.types.participant


class ConnectionTypeSummary(TypedDict):
    status: "aws_sdk_partnercentral_account.types.connection_type_status.ConnectionTypeStatus"
    """<p>The current status of this connection type (active, canceled, etc.).</p>"""
    other_participant: "aws_sdk_partnercentral_account.types.participant.Participant"
    """<p>Information about the other participant in this connection type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionTypeSummary) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_account.types.connection_type_status

    out["Status"] = (
        aws_sdk_partnercentral_account.types.connection_type_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import aws_sdk_partnercentral_account.types.participant

    out["OtherParticipant"] = (
        aws_sdk_partnercentral_account.types.participant.serialize_aws_json_1_0(
            value["other_participant"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionTypeSummary:
    out: ConnectionTypeSummary = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_partnercentral_account.types.connection_type_status

        out["status"] = (
            aws_sdk_partnercentral_account.types.connection_type_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ConnectionTypeSummary.status required")
    if "OtherParticipant" in data:
        import aws_sdk_partnercentral_account.types.participant

        out["other_participant"] = (
            aws_sdk_partnercentral_account.types.participant.deserialize_aws_json_1_0(
                data["OtherParticipant"]
            )
        )
    else:
        raise DeserializationError("ConnectionTypeSummary.other_participant required")
    return out
