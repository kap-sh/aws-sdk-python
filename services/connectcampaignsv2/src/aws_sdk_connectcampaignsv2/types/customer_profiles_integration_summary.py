"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CustomerProfilesIntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn
    import aws_sdk_connectcampaignsv2.types.object_type_names_map


class CustomerProfilesIntegrationSummary(TypedDict, closed=True):
    domain_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"
    object_type_names: (
        "aws_sdk_connectcampaignsv2.types.object_type_names_map.ObjectTypeNamesMap"
    )


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfilesIntegrationSummary) -> dict:
    out: dict = {}
    out["domainArn"] = value["domain_arn"]
    import aws_sdk_connectcampaignsv2.types.object_type_names_map

    out["objectTypeNames"] = (
        aws_sdk_connectcampaignsv2.types.object_type_names_map.serialize_json(
            value["object_type_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomerProfilesIntegrationSummary:
    out: CustomerProfilesIntegrationSummary = {}  # type: ignore[typeddict-item]
    if "domainArn" in data:
        out["domain_arn"] = data["domainArn"]
    else:
        raise DeserializationError(
            "CustomerProfilesIntegrationSummary.domain_arn required"
        )
    if "objectTypeNames" in data:
        import aws_sdk_connectcampaignsv2.types.object_type_names_map

        out["object_type_names"] = (
            aws_sdk_connectcampaignsv2.types.object_type_names_map.deserialize_json(
                data["objectTypeNames"]
            )
        )
    else:
        raise DeserializationError(
            "CustomerProfilesIntegrationSummary.object_type_names required"
        )
    return out
