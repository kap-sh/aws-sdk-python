"""Generated from Smithy shape ``com.amazonaws.route53domains#UpdateDomainNameserversRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name
    import aws_sdk_route_53_domains.types.fi_auth_key
    import aws_sdk_route_53_domains.types.nameserver_list


class UpdateDomainNameserversRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to change name servers for.</p>"""
    fi_auth_key: NotRequired["aws_sdk_route_53_domains.types.fi_auth_key.FIAuthKey"]
    """<p>The authorization key for .fi domains</p>"""
    nameservers: "aws_sdk_route_53_domains.types.nameserver_list.NameserverList"
    """<p>A list of new name servers for the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDomainNameserversRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "fi_auth_key" in value:
        out["FIAuthKey"] = value["fi_auth_key"]
    import aws_sdk_route_53_domains.types.nameserver_list

    out["Nameservers"] = (
        aws_sdk_route_53_domains.types.nameserver_list.serialize_aws_json_1_1(
            value["nameservers"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDomainNameserversRequest:
    out: UpdateDomainNameserversRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "UpdateDomainNameserversRequest.domain_name required"
        )
    if "FIAuthKey" in data:
        out["fi_auth_key"] = data["FIAuthKey"]
    if "Nameservers" in data:
        import aws_sdk_route_53_domains.types.nameserver_list

        out["nameservers"] = (
            aws_sdk_route_53_domains.types.nameserver_list.deserialize_aws_json_1_1(
                data["Nameservers"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDomainNameserversRequest.nameservers required"
        )
    return out
