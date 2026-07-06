"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListRecoveryPointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.recovery_point_list


class ListRecoveryPointsResponse(TypedDict, closed=True):
    recovery_points: NotRequired[
        "aws_sdk_redshift_serverless.types.recovery_point_list.RecoveryPointList"
    ]
    """<p>The returned recovery point objects.</p>"""
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRecoveryPointsResponse) -> dict:
    out: dict = {}
    if "recovery_points" in value:
        import aws_sdk_redshift_serverless.types.recovery_point_list

        out["recoveryPoints"] = (
            aws_sdk_redshift_serverless.types.recovery_point_list.serialize_aws_json_1_1(
                value["recovery_points"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRecoveryPointsResponse:
    out: ListRecoveryPointsResponse = {}  # type: ignore[typeddict-item]
    if "recoveryPoints" in data:
        import aws_sdk_redshift_serverless.types.recovery_point_list

        out["recovery_points"] = (
            aws_sdk_redshift_serverless.types.recovery_point_list.deserialize_aws_json_1_1(
                data["recoveryPoints"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
