"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.certificate_provider
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.setup_domain_name_list


class SetupRequest(TypedDict):
    instance_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the Lightsail instance.</p>"""
    domain_names: NotRequired[
        "aws_sdk_lightsail.types.setup_domain_name_list.SetupDomainNameList"
    ]
    """<p>The name of the domain and subdomains that the SSL/TLS certificate secures.</p>"""
    certificate_provider: NotRequired[
        "aws_sdk_lightsail.types.certificate_provider.CertificateProvider"
    ]
    """<p>The Certificate Authority (CA) that issues the SSL/TLS certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupRequest) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "domain_names" in value:
        import aws_sdk_lightsail.types.setup_domain_name_list

        out["domainNames"] = (
            aws_sdk_lightsail.types.setup_domain_name_list.serialize_aws_json_1_1(
                value["domain_names"]
            )
        )
    if "certificate_provider" in value:
        import aws_sdk_lightsail.types.certificate_provider

        out["certificateProvider"] = (
            aws_sdk_lightsail.types.certificate_provider.serialize_aws_json_1_1(
                value["certificate_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetupRequest:
    out: SetupRequest = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    if "domainNames" in data:
        import aws_sdk_lightsail.types.setup_domain_name_list

        out["domain_names"] = (
            aws_sdk_lightsail.types.setup_domain_name_list.deserialize_aws_json_1_1(
                data["domainNames"]
            )
        )
    if "certificateProvider" in data:
        import aws_sdk_lightsail.types.certificate_provider

        out["certificate_provider"] = (
            aws_sdk_lightsail.types.certificate_provider.deserialize_aws_json_1_1(
                data["certificateProvider"]
            )
        )
    return out
