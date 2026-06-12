"""Generated from Smithy shape ``com.amazonaws.outposts#AssetInstance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.account_id
    import aws_sdk_outposts.types.asset_id
    import aws_sdk_outposts.types.aws_service_name
    import aws_sdk_outposts.types.instance_id
    import aws_sdk_outposts.types.outpost_instance_type


class AssetInstance(TypedDict):
    instance_id: NotRequired["aws_sdk_outposts.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    instance_type: NotRequired[
        "aws_sdk_outposts.types.outpost_instance_type.OutpostInstanceType"
    ]
    """<p>The type of instance.</p>"""
    asset_id: NotRequired["aws_sdk_outposts.types.asset_id.AssetId"]
    """<p>The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    account_id: NotRequired["aws_sdk_outposts.types.account_id.AccountId"]
    aws_service_name: NotRequired[
        "aws_sdk_outposts.types.aws_service_name.AWSServiceName"
    ]
    """<p>The Amazon Web Services service name of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetInstance) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "asset_id" in value:
        out["AssetId"] = value["asset_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "aws_service_name" in value:
        import aws_sdk_outposts.types.aws_service_name

        out["AwsServiceName"] = aws_sdk_outposts.types.aws_service_name.serialize_json(
            value["aws_service_name"]
        )
    return out


def deserialize_json(data: dict) -> AssetInstance:
    out: AssetInstance = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
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
