"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#GetRelationshipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.relationship_detail


class GetRelationshipResponse(TypedDict):
    relationship_detail: NotRequired[
        "aws_sdk_partnercentral_channel.types.relationship_detail.RelationshipDetail"
    ]
    """<p>Details of the requested relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRelationshipResponse) -> dict:
    out: dict = {}
    if "relationship_detail" in value:
        import aws_sdk_partnercentral_channel.types.relationship_detail

        out["relationshipDetail"] = (
            aws_sdk_partnercentral_channel.types.relationship_detail.serialize_aws_json_1_0(
                value["relationship_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRelationshipResponse:
    out: GetRelationshipResponse = {}  # type: ignore[typeddict-item]
    if "relationshipDetail" in data:
        import aws_sdk_partnercentral_channel.types.relationship_detail

        out["relationship_detail"] = (
            aws_sdk_partnercentral_channel.types.relationship_detail.deserialize_aws_json_1_0(
                data["relationshipDetail"]
            )
        )
    return out
