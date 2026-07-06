"""Generated from Smithy shape ``com.amazonaws.odb#CrossRegionS3RestoreSourcesAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.managed_resource_status
    import aws_sdk_odb.types.string_list


class CrossRegionS3RestoreSourcesAccess(TypedDict, closed=True):
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region for cross-Region Amazon S3 restore access.</p>"""
    ipv4_addresses: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The IPv4 addresses allowed for cross-Region Amazon S3 restore access.</p>"""
    status: NotRequired[
        "aws_sdk_odb.types.managed_resource_status.ManagedResourceStatus"
    ]
    """<p>The current status of the cross-Region Amazon S3 restore access configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CrossRegionS3RestoreSourcesAccess) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "ipv4_addresses" in value:
        import aws_sdk_odb.types.string_list

        out["ipv4Addresses"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
            value["ipv4_addresses"]
        )
    if "status" in value:
        import aws_sdk_odb.types.managed_resource_status

        out["status"] = (
            aws_sdk_odb.types.managed_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CrossRegionS3RestoreSourcesAccess:
    out: CrossRegionS3RestoreSourcesAccess = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    if "ipv4Addresses" in data:
        import aws_sdk_odb.types.string_list

        out["ipv4_addresses"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["ipv4Addresses"]
        )
    if "status" in data:
        import aws_sdk_odb.types.managed_resource_status

        out["status"] = (
            aws_sdk_odb.types.managed_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
