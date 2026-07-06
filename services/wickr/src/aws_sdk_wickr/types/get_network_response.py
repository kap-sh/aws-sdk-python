"""Generated from Smithy shape ``com.amazonaws.wickr#GetNetworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.access_level
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id


class GetNetworkResponse(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The unique identifier of the network.</p>"""
    network_name: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The name of the network.</p>"""
    access_level: "aws_sdk_wickr.types.access_level.AccessLevel"
    """<p>The access level of the network (STANDARD or PREMIUM), which determines available features and capabilities.</p>"""
    aws_account_id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The Amazon Web Services account ID that owns the network.</p>"""
    network_arn: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the network.</p>"""
    standing: NotRequired["int"]
    """<p>The current standing or status of the network.</p>"""
    free_trial_expiration: NotRequired[
        "aws_sdk_wickr.types.generic_string.GenericString"
    ]
    """<p>The expiration date and time for the network's free trial period, if applicable.</p>"""
    migration_state: NotRequired["int"]
    """<p>The SSO redirect URI migration state, managed by the SSO redirect migration wizard. Values: 0 (not started), 1 (in progress), or 2 (completed).</p>"""
    encryption_key_arn: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The ARN of the Amazon Web Services KMS customer managed key used for encrypting sensitive data in the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkResponse) -> dict:
    out: dict = {}
    out["networkId"] = value["network_id"]
    out["networkName"] = value["network_name"]
    import aws_sdk_wickr.types.access_level

    out["accessLevel"] = aws_sdk_wickr.types.access_level.serialize_json(
        value["access_level"]
    )
    out["awsAccountId"] = value["aws_account_id"]
    out["networkArn"] = value["network_arn"]
    if "standing" in value:
        out["standing"] = value["standing"]
    if "free_trial_expiration" in value:
        out["freeTrialExpiration"] = value["free_trial_expiration"]
    if "migration_state" in value:
        out["migrationState"] = value["migration_state"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> GetNetworkResponse:
    out: GetNetworkResponse = {}  # type: ignore[typeddict-item]
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    else:
        raise DeserializationError("GetNetworkResponse.network_id required")
    if "networkName" in data:
        out["network_name"] = data["networkName"]
    else:
        raise DeserializationError("GetNetworkResponse.network_name required")
    if "accessLevel" in data:
        import aws_sdk_wickr.types.access_level

        out["access_level"] = aws_sdk_wickr.types.access_level.deserialize_json(
            data["accessLevel"]
        )
    else:
        raise DeserializationError("GetNetworkResponse.access_level required")
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    else:
        raise DeserializationError("GetNetworkResponse.aws_account_id required")
    if "networkArn" in data:
        out["network_arn"] = data["networkArn"]
    else:
        raise DeserializationError("GetNetworkResponse.network_arn required")
    if "standing" in data:
        out["standing"] = data["standing"]
    if "freeTrialExpiration" in data:
        out["free_trial_expiration"] = data["freeTrialExpiration"]
    if "migrationState" in data:
        out["migration_state"] = data["migrationState"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
