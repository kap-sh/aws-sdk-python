"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoEncryptionInfoDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details
    import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details


class AwsMskClusterClusterInfoEncryptionInfoDetails(TypedDict, closed=True):
    encryption_in_transit: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details.AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails"
    ]
    """<p> The settings for encrypting data in transit.</p>"""
    encryption_at_rest: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details.AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails"
    ]
    """<p> The data-volume encryption details. You can't update encryption at rest settings for existing clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsMskClusterClusterInfoEncryptionInfoDetails) -> dict:
    out: dict = {}
    if "encryption_in_transit" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details

        out["EncryptionInTransit"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details.serialize_json(
                value["encryption_in_transit"]
            )
        )
    if "encryption_at_rest" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details

        out["EncryptionAtRest"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details.serialize_json(
                value["encryption_at_rest"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsMskClusterClusterInfoEncryptionInfoDetails:
    out: AwsMskClusterClusterInfoEncryptionInfoDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionInTransit" in data:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details

        out["encryption_in_transit"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_in_transit_details.deserialize_json(
                data["EncryptionInTransit"]
            )
        )
    if "EncryptionAtRest" in data:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details

        out["encryption_at_rest"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_encryption_at_rest_details.deserialize_json(
                data["EncryptionAtRest"]
            )
        )
    return out
