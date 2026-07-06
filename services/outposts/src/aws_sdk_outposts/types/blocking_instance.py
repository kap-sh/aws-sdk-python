"""Generated from Smithy shape ``com.amazonaws.outposts#BlockingInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.account_id
    import aws_sdk_outposts.types.aws_service_name
    import aws_sdk_outposts.types.instance_id


class BlockingInstance(TypedDict, closed=True):
    instance_id: NotRequired["aws_sdk_outposts.types.instance_id.InstanceId"]
    """<p>The ID of the blocking instance.</p>"""
    account_id: NotRequired["aws_sdk_outposts.types.account_id.AccountId"]
    aws_service_name: NotRequired[
        "aws_sdk_outposts.types.aws_service_name.AWSServiceName"
    ]
    """<p>The Amazon Web Services service name that owns the specified blocking instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockingInstance) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "aws_service_name" in value:
        import aws_sdk_outposts.types.aws_service_name

        out["AwsServiceName"] = aws_sdk_outposts.types.aws_service_name.serialize_json(
            value["aws_service_name"]
        )
    return out


def deserialize_json(data: dict) -> BlockingInstance:
    out: BlockingInstance = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "AwsServiceName" in data:
        import aws_sdk_outposts.types.aws_service_name

        out["aws_service_name"] = (
            aws_sdk_outposts.types.aws_service_name.deserialize_json(
                data["AwsServiceName"]
            )
        )
    return out
