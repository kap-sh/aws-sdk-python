"""Generated from Smithy shape ``com.amazonaws.connect#BatchDisassociateAnalyticsDataSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.aws_account_id
    import aws_sdk_connect.types.data_set_ids
    import aws_sdk_connect.types.instance_id


class BatchDisassociateAnalyticsDataSetRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    data_set_ids: "aws_sdk_connect.types.data_set_ids.DataSetIds"
    """<p>An array of associated dataset identifiers to remove.</p>"""
    target_account_id: NotRequired["aws_sdk_connect.types.aws_account_id.AWSAccountId"]
    """<p>The identifier of the target account. Use to disassociate a dataset from a different account than the one containing the Connect Customer instance. If not specified, by default this value is the Amazon Web Services account that has the Connect Customer instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateAnalyticsDataSetRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.data_set_ids

    out["DataSetIds"] = aws_sdk_connect.types.data_set_ids.serialize_json(
        value["data_set_ids"]
    )
    if "target_account_id" in value:
        out["TargetAccountId"] = value["target_account_id"]
    return out


def deserialize_json(data: dict) -> BatchDisassociateAnalyticsDataSetRequest:
    out: BatchDisassociateAnalyticsDataSetRequest = {}  # type: ignore[typeddict-item]
    if "DataSetIds" in data:
        import aws_sdk_connect.types.data_set_ids

        out["data_set_ids"] = aws_sdk_connect.types.data_set_ids.deserialize_json(
            data["DataSetIds"]
        )
    else:
        raise DeserializationError(
            "BatchDisassociateAnalyticsDataSetRequest.data_set_ids required"
        )
    if "TargetAccountId" in data:
        out["target_account_id"] = data["TargetAccountId"]
    return out
