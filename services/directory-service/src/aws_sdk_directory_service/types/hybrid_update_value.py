"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridUpdateValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_instance_ids
    import aws_sdk_directory_service.types.customer_dns_ips


class HybridUpdateValue(TypedDict):
    instance_ids: NotRequired[
        "aws_sdk_directory_service.types.assessment_instance_ids.AssessmentInstanceIds"
    ]
    """<p>The identifiers of the self-managed instances with SSM in the hybrid directory configuration.</p>"""
    dns_ips: NotRequired[
        "aws_sdk_directory_service.types.customer_dns_ips.CustomerDnsIps"
    ]
    """<p>The IP addresses of the DNS servers or domain controllers in the hybrid directory configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridUpdateValue) -> dict:
    out: dict = {}
    if "instance_ids" in value:
        import aws_sdk_directory_service.types.assessment_instance_ids

        out["InstanceIds"] = (
            aws_sdk_directory_service.types.assessment_instance_ids.serialize_aws_json_1_1(
                value["instance_ids"]
            )
        )
    if "dns_ips" in value:
        import aws_sdk_directory_service.types.customer_dns_ips

        out["DnsIps"] = (
            aws_sdk_directory_service.types.customer_dns_ips.serialize_aws_json_1_1(
                value["dns_ips"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridUpdateValue:
    out: HybridUpdateValue = {}  # type: ignore[typeddict-item]
    if "InstanceIds" in data:
        import aws_sdk_directory_service.types.assessment_instance_ids

        out["instance_ids"] = (
            aws_sdk_directory_service.types.assessment_instance_ids.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    if "DnsIps" in data:
        import aws_sdk_directory_service.types.customer_dns_ips

        out["dns_ips"] = (
            aws_sdk_directory_service.types.customer_dns_ips.deserialize_aws_json_1_1(
                data["DnsIps"]
            )
        )
    return out
