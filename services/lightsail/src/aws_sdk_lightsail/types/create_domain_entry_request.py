"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDomainEntryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.domain_entry
    import aws_sdk_lightsail.types.domain_name


class CreateDomainEntryRequest(TypedDict):
    domain_name: "aws_sdk_lightsail.types.domain_name.DomainName"
    """<p>The domain name (<code>example.com</code>) for which you want to create the domain entry.</p>"""
    domain_entry: "aws_sdk_lightsail.types.domain_entry.DomainEntry"
    """<p>An array of key-value pairs containing information about the domain entry request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDomainEntryRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    import aws_sdk_lightsail.types.domain_entry

    out["domainEntry"] = aws_sdk_lightsail.types.domain_entry.serialize_aws_json_1_1(
        value["domain_entry"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDomainEntryRequest:
    out: CreateDomainEntryRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("CreateDomainEntryRequest.domain_name required")
    if "domainEntry" in data:
        import aws_sdk_lightsail.types.domain_entry

        out["domain_entry"] = (
            aws_sdk_lightsail.types.domain_entry.deserialize_aws_json_1_1(
                data["domainEntry"]
            )
        )
    else:
        raise DeserializationError("CreateDomainEntryRequest.domain_entry required")
    return out
