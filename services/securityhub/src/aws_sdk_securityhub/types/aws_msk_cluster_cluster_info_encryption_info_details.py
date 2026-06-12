"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoEncryptionInfoDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details
    import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details


class AwsMskClusterClusterInfoEncryptionInfoDetails(TypedDict):
    encryption_in_transit: NotRequired[
        "aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details.AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails"
    ]
    """<p> The settings for encrypting data in transit.</p>"""
    encryption_at_rest: NotRequired[
        "aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details.AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails"
    ]
    """<p> The data-volume encryption details. You can't update encryption at rest settings for existing clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsMskClusterClusterInfoEncryptionInfoDetails) -> dict:
    out: dict = {}
    if "encryption_in_transit" in value:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details

        out["EncryptionInTransit"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details.serialize_json(
                value["encryption_in_transit"]
            )
        )
    if "encryption_at_rest" in value:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details

        out["EncryptionAtRest"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details.serialize_json(
                value["encryption_at_rest"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsMskClusterClusterInfoEncryptionInfoDetails:
    out: AwsMskClusterClusterInfoEncryptionInfoDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionInTransit" in data:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details

        out["encryption_in_transit"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details.deserialize_json(
                data["EncryptionInTransit"]
            )
        )
    if "EncryptionAtRest" in data:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details

        out["encryption_at_rest"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details.deserialize_json(
                data["EncryptionAtRest"]
            )
        )
    return out
