"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateRelationshipDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.arn
    import aws_sdk_partnercentral_channel.types.relationship_id


class CreateRelationshipDetail(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the created relationship.</p>"""
    id: NotRequired[
        "aws_sdk_partnercentral_channel.types.relationship_id.RelationshipId"
    ]
    """<p>The unique identifier of the created relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRelationshipDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRelationshipDetail:
    out: CreateRelationshipDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    return out
