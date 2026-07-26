"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetRecoveryPointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.recovery_point


class GetRecoveryPointResponse(TypedDict, closed=True):
    recovery_point: NotRequired[
        "capo_redshift_serverless.types.recovery_point.RecoveryPoint"
    ]
    """<p>The returned recovery point object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRecoveryPointResponse) -> dict:
    out: dict = {}
    if "recovery_point" in value:
        import capo_redshift_serverless.types.recovery_point

        out["recoveryPoint"] = (
            capo_redshift_serverless.types.recovery_point.serialize_aws_json_1_1(
                value["recovery_point"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRecoveryPointResponse:
    out: GetRecoveryPointResponse = {}  # type: ignore[typeddict-item]
    if "recoveryPoint" in data:
        import capo_redshift_serverless.types.recovery_point

        out["recovery_point"] = (
            capo_redshift_serverless.types.recovery_point.deserialize_aws_json_1_1(
                data["recoveryPoint"]
            )
        )
    return out
