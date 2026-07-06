"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DescribeBackupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.backups
    import aws_sdk_cloudhsm_v2.types.next_token


class DescribeBackupsResponse(TypedDict, closed=True):
    backups: NotRequired["aws_sdk_cloudhsm_v2.types.backups.Backups"]
    """<p>A list of backups.</p>"""
    next_token: NotRequired["aws_sdk_cloudhsm_v2.types.next_token.NextToken"]
    """<p>An opaque string that indicates that the response contains only a subset of backups. Use this value in a subsequent <code>DescribeBackups</code> request to get more backups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBackupsResponse) -> dict:
    out: dict = {}
    if "backups" in value:
        import aws_sdk_cloudhsm_v2.types.backups

        out["Backups"] = aws_sdk_cloudhsm_v2.types.backups.serialize_aws_json_1_1(
            value["backups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBackupsResponse:
    out: DescribeBackupsResponse = {}  # type: ignore[typeddict-item]
    if "Backups" in data:
        import aws_sdk_cloudhsm_v2.types.backups

        out["backups"] = aws_sdk_cloudhsm_v2.types.backups.deserialize_aws_json_1_1(
            data["Backups"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
