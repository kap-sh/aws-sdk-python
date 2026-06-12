"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupInstanceHttpsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.certificate_provider
    import aws_sdk_lightsail.types.email_address
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.setup_domain_name_list


class SetupInstanceHttpsRequest(TypedDict):
    instance_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the Lightsail instance.</p>"""
    email_address: "aws_sdk_lightsail.types.email_address.EmailAddress"
    """<p>The contact method for SSL/TLS certificate renewal alerts. You can enter one email address. </p>"""
    domain_names: "aws_sdk_lightsail.types.setup_domain_name_list.SetupDomainNameList"
    """<p>The name of the domain and subdomains that were specified for the SSL/TLS certificate.</p>"""
    certificate_provider: (
        "aws_sdk_lightsail.types.certificate_provider.CertificateProvider"
    )
    """<p>The certificate authority that issues the SSL/TLS certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupInstanceHttpsRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    out["emailAddress"] = value["email_address"]
    import aws_sdk_lightsail.types.setup_domain_name_list

    out["domainNames"] = (
        aws_sdk_lightsail.types.setup_domain_name_list.serialize_aws_json_1_1(
            value["domain_names"]
        )
    )
    import aws_sdk_lightsail.types.certificate_provider

    out["certificateProvider"] = (
        aws_sdk_lightsail.types.certificate_provider.serialize_aws_json_1_1(
            value["certificate_provider"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetupInstanceHttpsRequest:
    out: SetupInstanceHttpsRequest = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("SetupInstanceHttpsRequest.instance_name required")
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    else:
        raise DeserializationError("SetupInstanceHttpsRequest.email_address required")
    if "domainNames" in data:
        import aws_sdk_lightsail.types.setup_domain_name_list

        out["domain_names"] = (
            aws_sdk_lightsail.types.setup_domain_name_list.deserialize_aws_json_1_1(
                data["domainNames"]
            )
        )
    else:
        raise DeserializationError("SetupInstanceHttpsRequest.domain_names required")
    if "certificateProvider" in data:
        import aws_sdk_lightsail.types.certificate_provider

        out["certificate_provider"] = (
            aws_sdk_lightsail.types.certificate_provider.deserialize_aws_json_1_1(
                data["certificateProvider"]
            )
        )
    else:
        raise DeserializationError(
            "SetupInstanceHttpsRequest.certificate_provider required"
        )
    return out
