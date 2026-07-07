"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PutProfileVisibilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.partner_arn
    import aws_sdk_partnercentral_account.types.partner_id
    import aws_sdk_partnercentral_account.types.partner_profile_id
    import aws_sdk_partnercentral_account.types.profile_visibility


class PutProfileVisibilityResponse(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "aws_sdk_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the partner account.</p>"""
    id: "aws_sdk_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    visibility: (
        "aws_sdk_partnercentral_account.types.profile_visibility.ProfileVisibility"
    )
    """<p>The updated visibility setting for the partner profile.</p>"""
    profile_id: (
        "aws_sdk_partnercentral_account.types.partner_profile_id.PartnerProfileId"
    )
    """<p>The unique identifier of the partner profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutProfileVisibilityResponse) -> dict:
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


def deserialize_aws_json_1_0(data: dict) -> PutProfileVisibilityResponse:
    out: PutProfileVisibilityResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("PutProfileVisibilityResponse.catalog required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("PutProfileVisibilityResponse.arn required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("PutProfileVisibilityResponse.id required")
    if "Visibility" in data:
        import aws_sdk_partnercentral_account.types.profile_visibility

        out["visibility"] = (
            aws_sdk_partnercentral_account.types.profile_visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    else:
        raise DeserializationError("PutProfileVisibilityResponse.visibility required")
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("PutProfileVisibilityResponse.profile_id required")
    return out
