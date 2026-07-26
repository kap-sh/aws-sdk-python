"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupInstanceHttpsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.certificate_provider
    import capo_lightsail.types.email_address
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.setup_domain_name_list


class SetupInstanceHttpsRequest(TypedDict, closed=True):
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the Lightsail instance.</p>"""
    email_address: "capo_lightsail.types.email_address.EmailAddress"
    """<p>The contact method for SSL/TLS certificate renewal alerts. You can enter one email address. </p>"""
    domain_names: "capo_lightsail.types.setup_domain_name_list.SetupDomainNameList"
    """<p>The name of the domain and subdomains that were specified for the SSL/TLS certificate.</p>"""
    certificate_provider: (
        "capo_lightsail.types.certificate_provider.CertificateProvider"
    )
    """<p>The certificate authority that issues the SSL/TLS certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupInstanceHttpsRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    out["emailAddress"] = value["email_address"]
    import capo_lightsail.types.setup_domain_name_list

    out["domainNames"] = (
        capo_lightsail.types.setup_domain_name_list.serialize_aws_json_1_1(
            value["domain_names"]
        )
    )
    import capo_lightsail.types.certificate_provider

    out["certificateProvider"] = (
        capo_lightsail.types.certificate_provider.serialize_aws_json_1_1(
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
        import capo_lightsail.types.setup_domain_name_list

        out["domain_names"] = (
            capo_lightsail.types.setup_domain_name_list.deserialize_aws_json_1_1(
                data["domainNames"]
            )
        )
    else:
        raise DeserializationError("SetupInstanceHttpsRequest.domain_names required")
    if "certificateProvider" in data:
        import capo_lightsail.types.certificate_provider

        out["certificate_provider"] = (
            capo_lightsail.types.certificate_provider.deserialize_aws_json_1_1(
                data["certificateProvider"]
            )
        )
    else:
        raise DeserializationError(
            "SetupInstanceHttpsRequest.certificate_provider required"
        )
    return out
