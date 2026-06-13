"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterMetadata``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.aws_ecs_metadata_details
    import aws_sdk_inspector2.types.aws_eks_metadata_details


class _ClusterMetadata_awsEcsMetadataDetails(TypedDict):
    awsEcsMetadataDetails: (
        "aws_sdk_inspector2.types.aws_ecs_metadata_details.AwsEcsMetadataDetails"
    )


class _ClusterMetadata_awsEksMetadataDetails(TypedDict):
    awsEksMetadataDetails: (
        "aws_sdk_inspector2.types.aws_eks_metadata_details.AwsEksMetadataDetails"
    )


ClusterMetadata: TypeAlias = (
    _ClusterMetadata_awsEcsMetadataDetails | _ClusterMetadata_awsEksMetadataDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: ClusterMetadata) -> dict:
    if "awsEcsMetadataDetails" in value:
        import aws_sdk_inspector2.types.aws_ecs_metadata_details

        return {
            "awsEcsMetadataDetails": aws_sdk_inspector2.types.aws_ecs_metadata_details.serialize_json(
                value["awsEcsMetadataDetails"]
            )
        }
    elif "awsEksMetadataDetails" in value:
        import aws_sdk_inspector2.types.aws_eks_metadata_details

        return {
            "awsEksMetadataDetails": aws_sdk_inspector2.types.aws_eks_metadata_details.serialize_json(
                value["awsEksMetadataDetails"]
            )
        }
    else:
        raise SerializationError("ClusterMetadata: no variant present")


def deserialize_json(data: dict) -> ClusterMetadata:
    if "awsEcsMetadataDetails" in data:
        import aws_sdk_inspector2.types.aws_ecs_metadata_details

        return {
            "awsEcsMetadataDetails": aws_sdk_inspector2.types.aws_ecs_metadata_details.deserialize_json(
                data["awsEcsMetadataDetails"]
            )
        }
    elif "awsEksMetadataDetails" in data:
        import aws_sdk_inspector2.types.aws_eks_metadata_details

        return {
            "awsEksMetadataDetails": aws_sdk_inspector2.types.aws_eks_metadata_details.deserialize_json(
                data["awsEksMetadataDetails"]
            )
        }
    else:
        raise DeserializationError("ClusterMetadata: no recognized variant key")
