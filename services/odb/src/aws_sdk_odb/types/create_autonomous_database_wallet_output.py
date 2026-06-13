"""Generated from Smithy shape ``com.amazonaws.odb#CreateAutonomousDatabaseWalletOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_wallet_file


class CreateAutonomousDatabaseWalletOutput(TypedDict):
    autonomous_database_wallet_file: (
        "aws_sdk_odb.types.autonomous_database_wallet_file.AutonomousDatabaseWalletFile"
    )
    """<p>The generated wallet file for the Autonomous Database, returned as a compressed archive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutonomousDatabaseWalletOutput) -> dict:
    out: dict = {}
    import aws_sdk_odb.types.autonomous_database_wallet_file

    out["autonomousDatabaseWalletFile"] = (
        aws_sdk_odb.types.autonomous_database_wallet_file.serialize_aws_json_1_0(
            value["autonomous_database_wallet_file"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutonomousDatabaseWalletOutput:
    out: CreateAutonomousDatabaseWalletOutput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseWalletFile" in data:
        import aws_sdk_odb.types.autonomous_database_wallet_file

        out["autonomous_database_wallet_file"] = (
            aws_sdk_odb.types.autonomous_database_wallet_file.deserialize_aws_json_1_0(
                data["autonomousDatabaseWalletFile"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAutonomousDatabaseWalletOutput.autonomous_database_wallet_file required"
        )
    return out
