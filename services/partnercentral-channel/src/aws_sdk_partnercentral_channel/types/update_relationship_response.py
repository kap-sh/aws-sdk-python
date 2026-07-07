"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#UpdateRelationshipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.update_relationship_detail


class UpdateRelationshipResponse(TypedDict, closed=True):
    relationship_detail: NotRequired[
        "aws_sdk_partnercentral_channel.types.update_relationship_detail.UpdateRelationshipDetail"
    ]
    """<p>Details of the updated relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRelationshipResponse) -> dict:
    out: dict = {}
    if "relationship_detail" in value:
        import aws_sdk_partnercentral_channel.types.update_relationship_detail

        out["relationshipDetail"] = (
            aws_sdk_partnercentral_channel.types.update_relationship_detail.serialize_aws_json_1_0(
                value["relationship_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRelationshipResponse:
    out: UpdateRelationshipResponse = {}  # type: ignore[typeddict-item]
    if "relationshipDetail" in data:
        import aws_sdk_partnercentral_channel.types.update_relationship_detail

        out["relationship_detail"] = (
            aws_sdk_partnercentral_channel.types.update_relationship_detail.deserialize_aws_json_1_0(
                data["relationshipDetail"]
            )
        )
    return out
