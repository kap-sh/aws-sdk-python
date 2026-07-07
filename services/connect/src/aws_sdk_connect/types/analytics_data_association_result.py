"""Generated from Smithy shape ``com.amazonaws.connect#AnalyticsDataAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.aws_account_id
    import aws_sdk_connect.types.data_set_id
    import aws_sdk_connect.types.string


class AnalyticsDataAssociationResult(TypedDict, closed=True):
    data_set_id: NotRequired["aws_sdk_connect.types.data_set_id.DataSetId"]
    """<p>The identifier of the dataset.</p>"""
    target_account_id: NotRequired["aws_sdk_connect.types.aws_account_id.AWSAccountId"]
    """<p>The identifier of the target account. </p>"""
    resource_share_id: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The Resource Access Manager share ID.</p>"""
    resource_share_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the Resource Access Manager share. </p>"""
    resource_share_status: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The Amazon Web Services Resource Access Manager status of association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsDataAssociationResult) -> dict:
    out: dict = {}
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "target_account_id" in value:
        out["TargetAccountId"] = value["target_account_id"]
    if "resource_share_id" in value:
        out["ResourceShareId"] = value["resource_share_id"]
    if "resource_share_arn" in value:
        out["ResourceShareArn"] = value["resource_share_arn"]
    if "resource_share_status" in value:
        out["ResourceShareStatus"] = value["resource_share_status"]
    return out


def deserialize_json(data: dict) -> AnalyticsDataAssociationResult:
    out: AnalyticsDataAssociationResult = {}  # type: ignore[typeddict-item]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    if "TargetAccountId" in data:
        out["target_account_id"] = data["TargetAccountId"]
    if "ResourceShareId" in data:
        out["resource_share_id"] = data["ResourceShareId"]
    if "ResourceShareArn" in data:
        out["resource_share_arn"] = data["ResourceShareArn"]
    if "ResourceShareStatus" in data:
        out["resource_share_status"] = data["ResourceShareStatus"]
    return out
