"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateOpsMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.metadata_keys_to_delete_list
    import aws_sdk_ssm.types.metadata_map
    import aws_sdk_ssm.types.ops_metadata_arn


class UpdateOpsMetadataRequest(TypedDict):
    ops_metadata_arn: "aws_sdk_ssm.types.ops_metadata_arn.OpsMetadataArn"
    """<p>The Amazon Resource Name (ARN) of the OpsMetadata Object to update.</p>"""
    metadata_to_update: NotRequired["aws_sdk_ssm.types.metadata_map.MetadataMap"]
    """<p>Metadata to add to an OpsMetadata object.</p>"""
    keys_to_delete: NotRequired[
        "aws_sdk_ssm.types.metadata_keys_to_delete_list.MetadataKeysToDeleteList"
    ]
    """<p>The metadata keys to delete from the OpsMetadata object. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOpsMetadataRequest) -> dict:
    out: dict = {}
    out["OpsMetadataArn"] = value["ops_metadata_arn"]
    if "metadata_to_update" in value:
        import aws_sdk_ssm.types.metadata_map

        out["MetadataToUpdate"] = aws_sdk_ssm.types.metadata_map.serialize_aws_json_1_1(
            value["metadata_to_update"]
        )
    if "keys_to_delete" in value:
        import aws_sdk_ssm.types.metadata_keys_to_delete_list

        out["KeysToDelete"] = (
            aws_sdk_ssm.types.metadata_keys_to_delete_list.serialize_aws_json_1_1(
                value["keys_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOpsMetadataRequest:
    out: UpdateOpsMetadataRequest = {}  # type: ignore[typeddict-item]
    if "OpsMetadataArn" in data:
        out["ops_metadata_arn"] = data["OpsMetadataArn"]
    else:
        raise DeserializationError("UpdateOpsMetadataRequest.ops_metadata_arn required")
    if "MetadataToUpdate" in data:
        import aws_sdk_ssm.types.metadata_map

        out["metadata_to_update"] = (
            aws_sdk_ssm.types.metadata_map.deserialize_aws_json_1_1(
                data["MetadataToUpdate"]
            )
        )
    if "KeysToDelete" in data:
        import aws_sdk_ssm.types.metadata_keys_to_delete_list

        out["keys_to_delete"] = (
            aws_sdk_ssm.types.metadata_keys_to_delete_list.deserialize_aws_json_1_1(
                data["KeysToDelete"]
            )
        )
    return out
