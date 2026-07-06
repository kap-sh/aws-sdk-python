"""Generated from Smithy shape ``com.amazonaws.odb#CreateAutonomousDatabaseWalletInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.general_input_string
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.sensitive_string
    import aws_sdk_odb.types.wallet_type


class CreateAutonomousDatabaseWalletInput(TypedDict, closed=True):
    autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to create a wallet for.</p>"""
    wallet_type: NotRequired["aws_sdk_odb.types.wallet_type.WalletType"]
    """<p>The type of wallet to create, either a regional wallet or an instance wallet.</p>"""
    password: "aws_sdk_odb.types.sensitive_string.SensitiveString"
    """<p>The password to encrypt the keys inside the wallet.</p>"""
    client_token: NotRequired[
        "aws_sdk_odb.types.general_input_string.GeneralInputString"
    ]
    """<p>A client-provided token to ensure the idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutonomousDatabaseWalletInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "wallet_type" in value:
        import aws_sdk_odb.types.wallet_type

        out["walletType"] = aws_sdk_odb.types.wallet_type.serialize_aws_json_1_0(
            value["wallet_type"]
        )
    out["password"] = value["password"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutonomousDatabaseWalletInput:
    out: CreateAutonomousDatabaseWalletInput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        raise DeserializationError(
            "CreateAutonomousDatabaseWalletInput.autonomous_database_id required"
        )
    if "walletType" in data:
        import aws_sdk_odb.types.wallet_type

        out["wallet_type"] = aws_sdk_odb.types.wallet_type.deserialize_aws_json_1_0(
            data["walletType"]
        )
    if "password" in data:
        out["password"] = data["password"]
    else:
        raise DeserializationError(
            "CreateAutonomousDatabaseWalletInput.password required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
