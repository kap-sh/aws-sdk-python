"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CustomerProfilesIntegrationIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn


class CustomerProfilesIntegrationIdentifier(TypedDict):
    domain_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfilesIntegrationIdentifier) -> dict:
    out: dict = {}
    out["domainArn"] = value["domain_arn"]
    return out


def deserialize_json(data: dict) -> CustomerProfilesIntegrationIdentifier:
    out: CustomerProfilesIntegrationIdentifier = {}  # type: ignore[typeddict-item]
    if "domainArn" in data:
        out["domain_arn"] = data["domainArn"]
    else:
        raise DeserializationError(
            "CustomerProfilesIntegrationIdentifier.domain_arn required"
        )
    return out
