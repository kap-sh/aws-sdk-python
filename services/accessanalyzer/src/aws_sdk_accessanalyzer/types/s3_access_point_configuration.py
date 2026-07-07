"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3AccessPointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.access_point_policy
    import aws_sdk_accessanalyzer.types.network_origin_configuration
    import aws_sdk_accessanalyzer.types.s3_public_access_block_configuration


class S3AccessPointConfiguration(TypedDict, closed=True):
    access_point_policy: NotRequired[
        "aws_sdk_accessanalyzer.types.access_point_policy.AccessPointPolicy"
    ]
    """<p>The access point or multi-region access point policy.</p>"""
    public_access_block: NotRequired[
        "aws_sdk_accessanalyzer.types.s3_public_access_block_configuration.S3PublicAccessBlockConfiguration"
    ]
    """<p>The proposed <code>S3PublicAccessBlock</code> configuration to apply to this Amazon S3 access point or multi-region access point.</p>"""
    network_origin: NotRequired[
        "aws_sdk_accessanalyzer.types.network_origin_configuration.NetworkOriginConfiguration"
    ]
    """<p>The proposed <code>Internet</code> and <code>VpcConfiguration</code> to apply to this Amazon S3 access point. <code>VpcConfiguration</code> does not apply to multi-region access points. If the access preview is for a new resource and neither is specified, the access preview uses <code>Internet</code> for the network origin. If the access preview is for an existing resource and neither is specified, the access preview uses the existing network origin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3AccessPointConfiguration) -> dict:
    out: dict = {}
    if "access_point_policy" in value:
        out["accessPointPolicy"] = value["access_point_policy"]
    if "public_access_block" in value:
        import aws_sdk_accessanalyzer.types.s3_public_access_block_configuration

        out["publicAccessBlock"] = (
            aws_sdk_accessanalyzer.types.s3_public_access_block_configuration.serialize_json(
                value["public_access_block"]
            )
        )
    if "network_origin" in value:
        import aws_sdk_accessanalyzer.types.network_origin_configuration

        out["networkOrigin"] = (
            aws_sdk_accessanalyzer.types.network_origin_configuration.serialize_json(
                value["network_origin"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3AccessPointConfiguration:
    out: S3AccessPointConfiguration = {}  # type: ignore[typeddict-item]
    if "accessPointPolicy" in data:
        out["access_point_policy"] = data["accessPointPolicy"]
    if "publicAccessBlock" in data:
        import aws_sdk_accessanalyzer.types.s3_public_access_block_configuration

        out["public_access_block"] = (
            aws_sdk_accessanalyzer.types.s3_public_access_block_configuration.deserialize_json(
                data["publicAccessBlock"]
            )
        )
    if "networkOrigin" in data:
        import aws_sdk_accessanalyzer.types.network_origin_configuration

        out["network_origin"] = (
            aws_sdk_accessanalyzer.types.network_origin_configuration.deserialize_json(
                data["networkOrigin"]
            )
        )
    return out
