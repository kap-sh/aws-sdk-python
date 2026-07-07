"""Generated from Smithy shape ``com.amazonaws.odb#GetAutonomousDatabaseWalletDetailsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_wallet_details


class GetAutonomousDatabaseWalletDetailsOutput(TypedDict, closed=True):
    autonomous_database_wallet_details: "aws_sdk_odb.types.autonomous_database_wallet_details.AutonomousDatabaseWalletDetails"
    """<p>The wallet details for the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutonomousDatabaseWalletDetailsOutput) -> dict:
    out: dict = {}
    import aws_sdk_odb.types.autonomous_database_wallet_details

    out["autonomousDatabaseWalletDetails"] = (
        aws_sdk_odb.types.autonomous_database_wallet_details.serialize_aws_json_1_0(
            value["autonomous_database_wallet_details"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutonomousDatabaseWalletDetailsOutput:
    out: GetAutonomousDatabaseWalletDetailsOutput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseWalletDetails" in data:
        import aws_sdk_odb.types.autonomous_database_wallet_details

        out["autonomous_database_wallet_details"] = (
            aws_sdk_odb.types.autonomous_database_wallet_details.deserialize_aws_json_1_0(
                data["autonomousDatabaseWalletDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutonomousDatabaseWalletDetailsOutput.autonomous_database_wallet_details required"
        )
    return out
