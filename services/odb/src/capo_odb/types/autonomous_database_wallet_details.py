"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseWalletDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.autonomous_database_wallet_status


class AutonomousDatabaseWalletDetails(TypedDict, closed=True):
    status: NotRequired[
        "capo_odb.types.autonomous_database_wallet_status.AutonomousDatabaseWalletStatus"
    ]
    """<p>The current status of the Autonomous Database wallet.</p>"""
    time_rotated: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database wallet was last rotated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseWalletDetails) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_odb.types.autonomous_database_wallet_status

        out["status"] = (
            capo_odb.types.autonomous_database_wallet_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "time_rotated" in value:
        import capo_odb.types._prelude.timestamp

        out["timeRotated"] = capo_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["time_rotated"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseWalletDetails:
    out: AutonomousDatabaseWalletDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_odb.types.autonomous_database_wallet_status

        out["status"] = (
            capo_odb.types.autonomous_database_wallet_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "timeRotated" in data:
        import capo_odb.types._prelude.timestamp

        out["time_rotated"] = (
            capo_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeRotated"]
            )
        )
    return out
