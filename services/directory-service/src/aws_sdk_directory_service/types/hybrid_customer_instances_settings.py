"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridCustomerInstancesSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_instance_ids
    import aws_sdk_directory_service.types.customer_dns_ips


class HybridCustomerInstancesSettings(TypedDict):
    customer_dns_ips: "aws_sdk_directory_service.types.customer_dns_ips.CustomerDnsIps"
    """<p>The IP addresses of the DNS servers or domain controllers in your self-managed AD environment.</p>"""
    instance_ids: (
        "aws_sdk_directory_service.types.assessment_instance_ids.AssessmentInstanceIds"
    )
    """<p>The identifiers of the self-managed instances with SSM used in hybrid directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridCustomerInstancesSettings) -> dict:
    out: dict = {}
    import aws_sdk_directory_service.types.customer_dns_ips

    out["CustomerDnsIps"] = (
        aws_sdk_directory_service.types.customer_dns_ips.serialize_aws_json_1_1(
            value["customer_dns_ips"]
        )
    )
    import aws_sdk_directory_service.types.assessment_instance_ids

    out["InstanceIds"] = (
        aws_sdk_directory_service.types.assessment_instance_ids.serialize_aws_json_1_1(
            value["instance_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridCustomerInstancesSettings:
    out: HybridCustomerInstancesSettings = {}  # type: ignore[typeddict-item]
    if "CustomerDnsIps" in data:
        import aws_sdk_directory_service.types.customer_dns_ips

        out["customer_dns_ips"] = (
            aws_sdk_directory_service.types.customer_dns_ips.deserialize_aws_json_1_1(
                data["CustomerDnsIps"]
            )
        )
    else:
        raise DeserializationError(
            "HybridCustomerInstancesSettings.customer_dns_ips required"
        )
    if "InstanceIds" in data:
        import aws_sdk_directory_service.types.assessment_instance_ids

        out["instance_ids"] = (
            aws_sdk_directory_service.types.assessment_instance_ids.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    else:
        raise DeserializationError(
            "HybridCustomerInstancesSettings.instance_ids required"
        )
    return out
