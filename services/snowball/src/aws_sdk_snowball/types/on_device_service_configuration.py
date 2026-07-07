"""Generated from Smithy shape ``com.amazonaws.snowball#OnDeviceServiceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.eks_on_device_service_configuration
    import aws_sdk_snowball.types.nfs_on_device_service_configuration
    import aws_sdk_snowball.types.s3_on_device_service_configuration
    import aws_sdk_snowball.types.tgw_on_device_service_configuration


class OnDeviceServiceConfiguration(TypedDict, closed=True):
    nfs_on_device_service: NotRequired[
        "aws_sdk_snowball.types.nfs_on_device_service_configuration.NFSOnDeviceServiceConfiguration"
    ]
    """<p>Represents the NFS (Network File System) service on a Snow Family device.</p>"""
    tgw_on_device_service: NotRequired[
        "aws_sdk_snowball.types.tgw_on_device_service_configuration.TGWOnDeviceServiceConfiguration"
    ]
    """<p>Represents the Storage Gateway service Tape Gateway type on a Snow Family device.</p>"""
    eks_on_device_service: NotRequired[
        "aws_sdk_snowball.types.eks_on_device_service_configuration.EKSOnDeviceServiceConfiguration"
    ]
    """<p>The configuration of EKS Anywhere on the Snow Family device.</p>"""
    s3_on_device_service: NotRequired[
        "aws_sdk_snowball.types.s3_on_device_service_configuration.S3OnDeviceServiceConfiguration"
    ]
    """<p>Configuration for Amazon S3 compatible storage on Snow family devices.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnDeviceServiceConfiguration) -> dict:
    out: dict = {}
    if "nfs_on_device_service" in value:
        import aws_sdk_snowball.types.nfs_on_device_service_configuration

        out["NFSOnDeviceService"] = (
            aws_sdk_snowball.types.nfs_on_device_service_configuration.serialize_aws_json_1_1(
                value["nfs_on_device_service"]
            )
        )
    if "tgw_on_device_service" in value:
        import aws_sdk_snowball.types.tgw_on_device_service_configuration

        out["TGWOnDeviceService"] = (
            aws_sdk_snowball.types.tgw_on_device_service_configuration.serialize_aws_json_1_1(
                value["tgw_on_device_service"]
            )
        )
    if "eks_on_device_service" in value:
        import aws_sdk_snowball.types.eks_on_device_service_configuration

        out["EKSOnDeviceService"] = (
            aws_sdk_snowball.types.eks_on_device_service_configuration.serialize_aws_json_1_1(
                value["eks_on_device_service"]
            )
        )
    if "s3_on_device_service" in value:
        import aws_sdk_snowball.types.s3_on_device_service_configuration

        out["S3OnDeviceService"] = (
            aws_sdk_snowball.types.s3_on_device_service_configuration.serialize_aws_json_1_1(
                value["s3_on_device_service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnDeviceServiceConfiguration:
    out: OnDeviceServiceConfiguration = {}  # type: ignore[typeddict-item]
    if "NFSOnDeviceService" in data:
        import aws_sdk_snowball.types.nfs_on_device_service_configuration

        out["nfs_on_device_service"] = (
            aws_sdk_snowball.types.nfs_on_device_service_configuration.deserialize_aws_json_1_1(
                data["NFSOnDeviceService"]
            )
        )
    if "TGWOnDeviceService" in data:
        import aws_sdk_snowball.types.tgw_on_device_service_configuration

        out["tgw_on_device_service"] = (
            aws_sdk_snowball.types.tgw_on_device_service_configuration.deserialize_aws_json_1_1(
                data["TGWOnDeviceService"]
            )
        )
    if "EKSOnDeviceService" in data:
        import aws_sdk_snowball.types.eks_on_device_service_configuration

        out["eks_on_device_service"] = (
            aws_sdk_snowball.types.eks_on_device_service_configuration.deserialize_aws_json_1_1(
                data["EKSOnDeviceService"]
            )
        )
    if "S3OnDeviceService" in data:
        import aws_sdk_snowball.types.s3_on_device_service_configuration

        out["s3_on_device_service"] = (
            aws_sdk_snowball.types.s3_on_device_service_configuration.deserialize_aws_json_1_1(
                data["S3OnDeviceService"]
            )
        )
    return out
