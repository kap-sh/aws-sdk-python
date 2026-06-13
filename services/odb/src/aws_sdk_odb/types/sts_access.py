"""Generated from Smithy shape ``com.amazonaws.odb#StsAccess``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.managed_resource_status
    import aws_sdk_odb.types.string_list


class StsAccess(TypedDict):
    status: NotRequired[
        "aws_sdk_odb.types.managed_resource_status.ManagedResourceStatus"
    ]
    """<p>The current status of the Amazon Web Services Security Token Service (STS) access configuration.</p>"""
    ipv4_addresses: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The IPv4 addresses allowed for Amazon Web Services Security Token Service (STS) access.</p>"""
    domain_name: NotRequired["str"]
    """<p>The domain name for Amazon Web Services Security Token Service (STS) access configuration.</p>"""
    sts_policy_document: NotRequired["str"]
    """<p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StsAccess) -> dict:
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
    if "sts_policy_document" in value:
        out["stsPolicyDocument"] = value["sts_policy_document"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StsAccess:
    out: StsAccess = {}  # type: ignore[typeddict-item]
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
    if "stsPolicyDocument" in data:
        out["sts_policy_document"] = data["stsPolicyDocument"]
    return out
