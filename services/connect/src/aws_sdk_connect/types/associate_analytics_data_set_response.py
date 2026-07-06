"""Generated from Smithy shape ``com.amazonaws.connect#AssociateAnalyticsDataSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.aws_account_id
    import aws_sdk_connect.types.data_set_id
    import aws_sdk_connect.types.string


class AssociateAnalyticsDataSetResponse(TypedDict, closed=True):
    data_set_id: NotRequired["aws_sdk_connect.types.data_set_id.DataSetId"]
    """<p>The identifier of the dataset that was associated.</p>"""
    target_account_id: NotRequired["aws_sdk_connect.types.aws_account_id.AWSAccountId"]
    """<p>The identifier of the target account. </p>"""
    resource_share_id: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The Resource Access Manager share ID that is generated.</p>"""
    resource_share_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the Resource Access Manager share. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAnalyticsDataSetResponse) -> dict:
    out: dict = {}
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "target_account_id" in value:
        out["TargetAccountId"] = value["target_account_id"]
    if "resource_share_id" in value:
        out["ResourceShareId"] = value["resource_share_id"]
    if "resource_share_arn" in value:
        out["ResourceShareArn"] = value["resource_share_arn"]
    return out


def deserialize_json(data: dict) -> AssociateAnalyticsDataSetResponse:
    out: AssociateAnalyticsDataSetResponse = {}  # type: ignore[typeddict-item]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    if "TargetAccountId" in data:
        out["target_account_id"] = data["TargetAccountId"]
    if "ResourceShareId" in data:
        out["resource_share_id"] = data["ResourceShareId"]
    if "ResourceShareArn" in data:
        out["resource_share_arn"] = data["ResourceShareArn"]
    return out
