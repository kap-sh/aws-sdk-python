"""Generated from Smithy shape ``com.amazonaws.dataexchange#ReceivedDataGrantSummariesEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.data_grant_acceptance_state
    import capo_dataexchange.types.data_grant_name
    import capo_dataexchange.types.id
    import capo_dataexchange.types.receiver_principal
    import capo_dataexchange.types.sender_principal
    import capo_dataexchange.types.timestamp


class ReceivedDataGrantSummariesEntry(TypedDict, closed=True):
    name: "capo_dataexchange.types.data_grant_name.DataGrantName"
    """<p>The name of the data grant.</p>"""
    sender_principal: "capo_dataexchange.types.sender_principal.SenderPrincipal"
    """<p>The Amazon Web Services account ID of the data grant sender.</p>"""
    receiver_principal: "capo_dataexchange.types.receiver_principal.ReceiverPrincipal"
    """<p>The Amazon Web Services account ID of the data grant receiver.</p>"""
    acceptance_state: (
        "capo_dataexchange.types.data_grant_acceptance_state.DataGrantAcceptanceState"
    )
    """<p>The acceptance state of the data grant.</p>"""
    accepted_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when the data grant was accepted.</p>"""
    ends_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when access to the associated data set ends.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data set associated to the data grant.</p>"""
    id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data grant.</p>"""
    arn: "capo_dataexchange.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data grant.</p>"""
    created_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was created.</p>"""
    updated_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReceivedDataGrantSummariesEntry) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["SenderPrincipal"] = value["sender_principal"]
    out["ReceiverPrincipal"] = value["receiver_principal"]
    out["AcceptanceState"] = value["acceptance_state"]
    if "accepted_at" in value:
        import capo_dataexchange.types.timestamp

        out["AcceptedAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["accepted_at"]
        )
    if "ends_at" in value:
        import capo_dataexchange.types.timestamp

        out["EndsAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["ends_at"]
        )
    out["DataSetId"] = value["data_set_id"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import capo_dataexchange.types.timestamp

    out["CreatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_dataexchange.types.timestamp

    out["UpdatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ReceivedDataGrantSummariesEntry:
    out: ReceivedDataGrantSummariesEntry = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ReceivedDataGrantSummariesEntry.name required")
    if "SenderPrincipal" in data:
        out["sender_principal"] = data["SenderPrincipal"]
    else:
        raise DeserializationError(
            "ReceivedDataGrantSummariesEntry.sender_principal required"
        )
    if "ReceiverPrincipal" in data:
        out["receiver_principal"] = data["ReceiverPrincipal"]
    else:
        raise DeserializationError(
            "ReceivedDataGrantSummariesEntry.receiver_principal required"
        )
    if "AcceptanceState" in data:
        out["acceptance_state"] = data["AcceptanceState"]
    else:
        raise DeserializationError(
            "ReceivedDataGrantSummariesEntry.acceptance_state required"
        )
    if "AcceptedAt" in data:
        import capo_dataexchange.types.timestamp

        out["accepted_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["AcceptedAt"]
        )
    if "EndsAt" in data:
        import capo_dataexchange.types.timestamp

        out["ends_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["EndsAt"]
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ReceivedDataGrantSummariesEntry.data_set_id required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("ReceivedDataGrantSummariesEntry.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ReceivedDataGrantSummariesEntry.arn required")
    if "CreatedAt" in data:
        import capo_dataexchange.types.timestamp

        out["created_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError(
            "ReceivedDataGrantSummariesEntry.created_at required"
        )
    if "UpdatedAt" in data:
        import capo_dataexchange.types.timestamp

        out["updated_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError(
            "ReceivedDataGrantSummariesEntry.updated_at required"
        )
    return out
