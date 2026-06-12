"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CancelConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.connection_id
    import aws_sdk_partnercentral_account.types.connection_type


class CancelConnectionRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection exists.</p>"""
    identifier: "aws_sdk_partnercentral_account.types.connection_id.ConnectionId"
    """<p>The unique identifier of the connection to cancel.</p>"""
    connection_type: (
        "aws_sdk_partnercentral_account.types.connection_type.ConnectionType"
    )
    """<p>The type of connection to cancel (e.g., reseller, distributor, technology partner).</p>"""
    reason: "str"
    """<p>The reason for canceling the connection, providing context for the termination.</p>"""
    client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelConnectionRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    import aws_sdk_partnercentral_account.types.connection_type

    out["ConnectionType"] = (
        aws_sdk_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
            value["connection_type"]
        )
    )
    out["Reason"] = value["reason"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelConnectionRequest:
    out: CancelConnectionRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CancelConnectionRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("CancelConnectionRequest.identifier required")
    if "ConnectionType" in data:
        import aws_sdk_partnercentral_account.types.connection_type

        out["connection_type"] = (
            aws_sdk_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                data["ConnectionType"]
            )
        )
    else:
        raise DeserializationError("CancelConnectionRequest.connection_type required")
    if "Reason" in data:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("CancelConnectionRequest.reason required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CancelConnectionRequest.client_token required")
    return out
