"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.aws_account_id
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.connection_arn
    import aws_sdk_partnercentral_account.types.connection_id
    import aws_sdk_partnercentral_account.types.connection_type_detail_map
    import aws_sdk_partnercentral_account.types.date_time


class Connection(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier that the connection belongs to.</p>"""
    id: "aws_sdk_partnercentral_account.types.connection_id.ConnectionId"
    """<p>The unique identifier of the connection.</p>"""
    arn: "aws_sdk_partnercentral_account.types.connection_arn.ConnectionArn"
    """<p>The AWS Resource Name (ARN) of the connection.</p>"""
    other_participant_account_id: (
        "aws_sdk_partnercentral_account.types.aws_account_id.AwsAccountId"
    )
    """<p>The AWS account ID of the other participant in the connection.</p>"""
    updated_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection was last updated.</p>"""
    connection_types: "aws_sdk_partnercentral_account.types.connection_type_detail_map.ConnectionTypeDetailMap"
    """<p>The type of connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Connection) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    out["OtherParticipantAccountId"] = value["other_participant_account_id"]
    import aws_sdk_partnercentral_account.types.date_time

    out["UpdatedAt"] = (
        aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    import aws_sdk_partnercentral_account.types.connection_type_detail_map

    out["ConnectionTypes"] = (
        aws_sdk_partnercentral_account.types.connection_type_detail_map.serialize_aws_json_1_0(
            value["connection_types"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("Connection.catalog required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Connection.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Connection.arn required")
    if "OtherParticipantAccountId" in data:
        out["other_participant_account_id"] = data["OtherParticipantAccountId"]
    else:
        raise DeserializationError("Connection.other_participant_account_id required")
    if "UpdatedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["updated_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError("Connection.updated_at required")
    if "ConnectionTypes" in data:
        import aws_sdk_partnercentral_account.types.connection_type_detail_map

        out["connection_types"] = (
            aws_sdk_partnercentral_account.types.connection_type_detail_map.deserialize_aws_json_1_0(
                data["ConnectionTypes"]
            )
        )
    else:
        raise DeserializationError("Connection.connection_types required")
    return out
