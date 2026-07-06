"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PublicDnsPropertiesMutable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.soa


class PublicDnsPropertiesMutable(TypedDict, closed=True):
    soa: "aws_sdk_servicediscovery.types.soa.SOA"
    """<p>Start of Authority (SOA) record for the hosted zone for the public DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicDnsPropertiesMutable) -> dict:
    out: dict = {}
    import aws_sdk_servicediscovery.types.soa

    out["SOA"] = aws_sdk_servicediscovery.types.soa.serialize_aws_json_1_1(value["soa"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicDnsPropertiesMutable:
    out: PublicDnsPropertiesMutable = {}  # type: ignore[typeddict-item]
    if "SOA" in data:
        import aws_sdk_servicediscovery.types.soa

        out["soa"] = aws_sdk_servicediscovery.types.soa.deserialize_aws_json_1_1(
            data["SOA"]
        )
    else:
        raise DeserializationError("PublicDnsPropertiesMutable.soa required")
    return out
