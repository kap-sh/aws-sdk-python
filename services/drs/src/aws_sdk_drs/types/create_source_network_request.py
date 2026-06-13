"""Generated from Smithy shape ``com.amazonaws.drs#CreateSourceNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.account_id
    import aws_sdk_drs.types.aws_region
    import aws_sdk_drs.types.tags_map
    import aws_sdk_drs.types.vpc_id


class CreateSourceNetworkRequest(TypedDict):
    vpc_id: "aws_sdk_drs.types.vpc_id.VpcID"
    """<p>Which VPC ID to protect.</p>"""
    origin_account_id: "aws_sdk_drs.types.account_id.AccountID"
    """<p>Account containing the VPC to protect.</p>"""
    origin_region: "aws_sdk_drs.types.aws_region.AwsRegion"
    """<p>Region containing the VPC to protect.</p>"""
    tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>A set of tags to be associated with the Source Network resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSourceNetworkRequest) -> dict:
    out: dict = {}
    out["vpcID"] = value["vpc_id"]
    out["originAccountID"] = value["origin_account_id"]
    out["originRegion"] = value["origin_region"]
    if "tags" in value:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSourceNetworkRequest:
    out: CreateSourceNetworkRequest = {}  # type: ignore[typeddict-item]
    if "vpcID" in data:
        out["vpc_id"] = data["vpcID"]
    else:
        raise DeserializationError("CreateSourceNetworkRequest.vpc_id required")
    if "originAccountID" in data:
        out["origin_account_id"] = data["originAccountID"]
    else:
        raise DeserializationError(
            "CreateSourceNetworkRequest.origin_account_id required"
        )
    if "originRegion" in data:
        out["origin_region"] = data["originRegion"]
    else:
        raise DeserializationError("CreateSourceNetworkRequest.origin_region required")
    if "tags" in data:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    return out
