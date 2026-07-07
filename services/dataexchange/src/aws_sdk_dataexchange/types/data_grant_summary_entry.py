"""Generated from Smithy shape ``com.amazonaws.dataexchange#DataGrantSummaryEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.arn
    import aws_sdk_dataexchange.types.data_grant_acceptance_state
    import aws_sdk_dataexchange.types.data_grant_name
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.receiver_principal
    import aws_sdk_dataexchange.types.sender_principal
    import aws_sdk_dataexchange.types.timestamp


class DataGrantSummaryEntry(TypedDict, closed=True):
    name: "aws_sdk_dataexchange.types.data_grant_name.DataGrantName"
    """<p>The name of the data grant.</p>"""
    sender_principal: "aws_sdk_dataexchange.types.sender_principal.SenderPrincipal"
    """<p>The Amazon Web Services account ID of the data grant sender.</p>"""
    receiver_principal: (
        "aws_sdk_dataexchange.types.receiver_principal.ReceiverPrincipal"
    )
    """<p>The Amazon Web Services account ID of the data grant receiver.</p>"""
    acceptance_state: "aws_sdk_dataexchange.types.data_grant_acceptance_state.DataGrantAcceptanceState"
    """<p>The acceptance state of the data grant.</p>"""
    accepted_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when the data grant was accepted.</p>"""
    ends_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when access to the associated data set ends.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The ID of the data set associated to the data grant.</p>"""
    source_data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The ID of the data set used to create the data grant.</p>"""
    id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The ID of the data grant.</p>"""
    arn: "aws_sdk_dataexchange.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data grant.</p>"""
    created_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was created.</p>"""
    updated_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataGrantSummaryEntry) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["SenderPrincipal"] = value["sender_principal"]
    out["ReceiverPrincipal"] = value["receiver_principal"]
    out["AcceptanceState"] = value["acceptance_state"]
    if "accepted_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["AcceptedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["accepted_at"]
        )
    if "ends_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["EndsAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["ends_at"]
        )
    out["DataSetId"] = value["data_set_id"]
    out["SourceDataSetId"] = value["source_data_set_id"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import aws_sdk_dataexchange.types.timestamp

    out["CreatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_dataexchange.types.timestamp

    out["UpdatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DataGrantSummaryEntry:
    out: DataGrantSummaryEntry = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DataGrantSummaryEntry.name required")
    if "SenderPrincipal" in data:
        out["sender_principal"] = data["SenderPrincipal"]
    else:
        raise DeserializationError("DataGrantSummaryEntry.sender_principal required")
    if "ReceiverPrincipal" in data:
        out["receiver_principal"] = data["ReceiverPrincipal"]
    else:
        raise DeserializationError("DataGrantSummaryEntry.receiver_principal required")
    if "AcceptanceState" in data:
        out["acceptance_state"] = data["AcceptanceState"]
    else:
        raise DeserializationError("DataGrantSummaryEntry.acceptance_state required")
    if "AcceptedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["accepted_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["AcceptedAt"]
        )
    if "EndsAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["ends_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["EndsAt"]
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError("DataGrantSummaryEntry.data_set_id required")
    if "SourceDataSetId" in data:
        out["source_data_set_id"] = data["SourceDataSetId"]
    else:
        raise DeserializationError("DataGrantSummaryEntry.source_data_set_id required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DataGrantSummaryEntry.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DataGrantSummaryEntry.arn required")
    if "CreatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["created_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("DataGrantSummaryEntry.created_at required")
    if "UpdatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["updated_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("DataGrantSummaryEntry.updated_at required")
    return out
