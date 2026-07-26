"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.aws_account_id
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_arn
    import capo_partnercentral_account.types.connection_id
    import capo_partnercentral_account.types.connection_type_detail_map
    import capo_partnercentral_account.types.date_time


class GetConnectionResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection exists.</p>"""
    id: "capo_partnercentral_account.types.connection_id.ConnectionId"
    """<p>The unique identifier of the connection.</p>"""
    arn: "capo_partnercentral_account.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection.</p>"""
    other_participant_account_id: (
        "capo_partnercentral_account.types.aws_account_id.AwsAccountId"
    )
    """<p>The AWS account ID of the other participant in the connection.</p>"""
    updated_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection was last updated.</p>"""
    connection_types: "capo_partnercentral_account.types.connection_type_detail_map.ConnectionTypeDetailMap"
    """<p>The list of connection types active between the partners.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    out["OtherParticipantAccountId"] = value["other_participant_account_id"]
    import capo_partnercentral_account.types.date_time

    out["UpdatedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    import capo_partnercentral_account.types.connection_type_detail_map

    out["ConnectionTypes"] = (
        capo_partnercentral_account.types.connection_type_detail_map.serialize_aws_json_1_0(
            value["connection_types"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionResponse:
    out: GetConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetConnectionResponse.catalog required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetConnectionResponse.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetConnectionResponse.arn required")
    if "OtherParticipantAccountId" in data:
        out["other_participant_account_id"] = data["OtherParticipantAccountId"]
    else:
        raise DeserializationError(
            "GetConnectionResponse.other_participant_account_id required"
        )
    if "UpdatedAt" in data:
        import capo_partnercentral_account.types.date_time

        out["updated_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError("GetConnectionResponse.updated_at required")
    if "ConnectionTypes" in data:
        import capo_partnercentral_account.types.connection_type_detail_map

        out["connection_types"] = (
            capo_partnercentral_account.types.connection_type_detail_map.deserialize_aws_json_1_0(
                data["ConnectionTypes"]
            )
        )
    else:
        raise DeserializationError("GetConnectionResponse.connection_types required")
    return out
