"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetProfileVisibilityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.partner_arn
    import aws_sdk_partnercentral_account.types.partner_id
    import aws_sdk_partnercentral_account.types.partner_profile_id
    import aws_sdk_partnercentral_account.types.profile_visibility


class GetProfileVisibilityResponse(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "aws_sdk_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the partner account.</p>"""
    id: "aws_sdk_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    visibility: (
        "aws_sdk_partnercentral_account.types.profile_visibility.ProfileVisibility"
    )
    """<p>The visibility setting for the partner profile (public, private, restricted, etc.).</p>"""
    profile_id: (
        "aws_sdk_partnercentral_account.types.partner_profile_id.PartnerProfileId"
    )
    """<p>The unique identifier of the partner profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProfileVisibilityResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    import aws_sdk_partnercentral_account.types.profile_visibility

    out["Visibility"] = (
        aws_sdk_partnercentral_account.types.profile_visibility.serialize_aws_json_1_0(
            value["visibility"]
        )
    )
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProfileVisibilityResponse:
    out: GetProfileVisibilityResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetProfileVisibilityResponse.catalog required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetProfileVisibilityResponse.arn required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetProfileVisibilityResponse.id required")
    if "Visibility" in data:
        import aws_sdk_partnercentral_account.types.profile_visibility

        out["visibility"] = (
            aws_sdk_partnercentral_account.types.profile_visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    else:
        raise DeserializationError("GetProfileVisibilityResponse.visibility required")
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("GetProfileVisibilityResponse.profile_id required")
    return out
