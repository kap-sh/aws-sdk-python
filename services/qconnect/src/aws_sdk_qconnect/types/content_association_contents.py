"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentAssociationContents``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.amazon_connect_guide_association_data


class _ContentAssociationContents_amazonConnectGuideAssociation(TypedDict, closed=True):
    amazonConnectGuideAssociation: "aws_sdk_qconnect.types.amazon_connect_guide_association_data.AmazonConnectGuideAssociationData"


ContentAssociationContents: TypeAlias = (
    _ContentAssociationContents_amazonConnectGuideAssociation
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentAssociationContents) -> dict:
    if "amazonConnectGuideAssociation" in value:
        import aws_sdk_qconnect.types.amazon_connect_guide_association_data

        return {
            "amazonConnectGuideAssociation": aws_sdk_qconnect.types.amazon_connect_guide_association_data.serialize_json(
                value["amazonConnectGuideAssociation"]
            )
        }
    else:
        raise SerializationError("ContentAssociationContents: no variant present")


def deserialize_json(data: dict) -> ContentAssociationContents:
    if "amazonConnectGuideAssociation" in data:
        import aws_sdk_qconnect.types.amazon_connect_guide_association_data

        return {
            "amazonConnectGuideAssociation": aws_sdk_qconnect.types.amazon_connect_guide_association_data.deserialize_json(
                data["amazonConnectGuideAssociation"]
            )
        }
    else:
        raise DeserializationError(
            "ContentAssociationContents: no recognized variant key"
        )
