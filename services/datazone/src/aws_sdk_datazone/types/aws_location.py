"""Generated from Smithy shape ``com.amazonaws.datazone#AwsLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.connection_id


class AwsLocation(TypedDict):
    access_role: NotRequired["str"]
    """<p>The access role of a connection.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The account ID of a connection.</p>"""
    aws_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Region of a connection.</p>"""
    iam_connection_id: NotRequired["aws_sdk_datazone.types.connection_id.ConnectionId"]
    """<p>The IAM connection ID of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLocation) -> dict:
    out: dict = {}
    if "access_role" in value:
        out["accessRole"] = value["access_role"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "iam_connection_id" in value:
        out["iamConnectionId"] = value["iam_connection_id"]
    return out


def deserialize_json(data: dict) -> AwsLocation:
    out: AwsLocation = {}  # type: ignore[typeddict-item]
    if "accessRole" in data:
        out["access_role"] = data["accessRole"]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    if "iamConnectionId" in data:
        out["iam_connection_id"] = data["iamConnectionId"]
    return out
