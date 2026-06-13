"""Generated from Smithy shape ``com.amazonaws.entityresolution#CustomerProfilesIntegrationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.customer_profiles_domain_arn
    import aws_sdk_entityresolution.types.customer_profiles_object_type_arn


class CustomerProfilesIntegrationConfig(TypedDict):
    domain_arn: "aws_sdk_entityresolution.types.customer_profiles_domain_arn.CustomerProfilesDomainArn"
    """<p>The Amazon Resource Name (ARN) of the Customer Profiles domain where the matched output will be sent.</p>"""
    object_type_arn: "aws_sdk_entityresolution.types.customer_profiles_object_type_arn.CustomerProfilesObjectTypeArn"
    """<p>The Amazon Resource Name (ARN) of the Customer Profiles object type that defines the structure for the matched customer data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfilesIntegrationConfig) -> dict:
    out: dict = {}
    out["domainArn"] = value["domain_arn"]
    out["objectTypeArn"] = value["object_type_arn"]
    return out


def deserialize_json(data: dict) -> CustomerProfilesIntegrationConfig:
    out: CustomerProfilesIntegrationConfig = {}  # type: ignore[typeddict-item]
    if "domainArn" in data:
        out["domain_arn"] = data["domainArn"]
    else:
        raise DeserializationError(
            "CustomerProfilesIntegrationConfig.domain_arn required"
        )
    if "objectTypeArn" in data:
        out["object_type_arn"] = data["objectTypeArn"]
    else:
        raise DeserializationError(
            "CustomerProfilesIntegrationConfig.object_type_arn required"
        )
    return out
