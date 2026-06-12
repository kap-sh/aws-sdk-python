"""Generated from Smithy shape ``com.amazonaws.outposts#ListAssetInstancesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_instance_list
    import aws_sdk_outposts.types.token


class ListAssetInstancesOutput(TypedDict):
    asset_instances: NotRequired[
        "aws_sdk_outposts.types.asset_instance_list.AssetInstanceList"
    ]
    """<p>List of instances owned by all accounts on the Outpost. Does not include Amazon EBS or Amazon S3 instances.</p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetInstancesOutput) -> dict:
    out: dict = {}
    if "asset_instances" in value:
        import aws_sdk_outposts.types.asset_instance_list

        out["AssetInstances"] = (
            aws_sdk_outposts.types.asset_instance_list.serialize_json(
                value["asset_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetInstancesOutput:
    out: ListAssetInstancesOutput = {}  # type: ignore[typeddict-item]
    if "AssetInstances" in data:
        import aws_sdk_outposts.types.asset_instance_list

        out["asset_instances"] = (
            aws_sdk_outposts.types.asset_instance_list.deserialize_json(
                data["AssetInstances"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
