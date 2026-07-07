"""Generated from Smithy shape ``com.amazonaws.odb#S3Access``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.managed_resource_status
    import aws_sdk_odb.types.string_list


class S3Access(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_odb.types.managed_resource_status.ManagedResourceStatus"
    ]
    """<p>The status of the Amazon S3 access.</p>"""
    ipv4_addresses: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The IPv4 addresses for the Amazon S3 access.</p>"""
    domain_name: NotRequired["str"]
    """<p>The domain name for the Amazon S3 access.</p>"""
    s3_policy_document: NotRequired["str"]
    """<p>The endpoint policy for the Amazon S3 access.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Access) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_odb.types.managed_resource_status

        out["status"] = (
            aws_sdk_odb.types.managed_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "ipv4_addresses" in value:
        import aws_sdk_odb.types.string_list

        out["ipv4Addresses"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
            value["ipv4_addresses"]
        )
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "s3_policy_document" in value:
        out["s3PolicyDocument"] = value["s3_policy_document"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Access:
    out: S3Access = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_odb.types.managed_resource_status

        out["status"] = (
            aws_sdk_odb.types.managed_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "ipv4Addresses" in data:
        import aws_sdk_odb.types.string_list

        out["ipv4_addresses"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["ipv4Addresses"]
        )
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "s3PolicyDocument" in data:
        out["s3_policy_document"] = data["s3PolicyDocument"]
    return out
