"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeBackupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.backups
    import capo_fsx.types.next_token


class DescribeBackupsResponse(TypedDict, closed=True):
    backups: NotRequired["capo_fsx.types.backups.Backups"]
    """<p>An array of backups.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]
    """<p>A <code>NextToken</code> value is present if there are more backups than returned in the response. You can use the <code>NextToken</code> value in the subsequent request to fetch the backups. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBackupsResponse) -> dict:
    out: dict = {}
    if "backups" in value:
        import capo_fsx.types.backups

        out["Backups"] = capo_fsx.types.backups.serialize_aws_json_1_1(value["backups"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBackupsResponse:
    out: DescribeBackupsResponse = {}  # type: ignore[typeddict-item]
    if "Backups" in data:
        import capo_fsx.types.backups

        out["backups"] = capo_fsx.types.backups.deserialize_aws_json_1_1(
            data["Backups"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
