"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateRelationshipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.create_relationship_detail


class CreateRelationshipResponse(TypedDict):
    relationship_detail: NotRequired[
        "aws_sdk_partnercentral_channel.types.create_relationship_detail.CreateRelationshipDetail"
    ]
    """<p>Details of the created relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRelationshipResponse) -> dict:
    out: dict = {}
    if "relationship_detail" in value:
        import aws_sdk_partnercentral_channel.types.create_relationship_detail

        out["relationshipDetail"] = (
            aws_sdk_partnercentral_channel.types.create_relationship_detail.serialize_aws_json_1_0(
                value["relationship_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRelationshipResponse:
    out: CreateRelationshipResponse = {}  # type: ignore[typeddict-item]
    if "relationshipDetail" in data:
        import aws_sdk_partnercentral_channel.types.create_relationship_detail

        out["relationship_detail"] = (
            aws_sdk_partnercentral_channel.types.create_relationship_detail.deserialize_aws_json_1_0(
                data["relationshipDetail"]
            )
        )
    return out
