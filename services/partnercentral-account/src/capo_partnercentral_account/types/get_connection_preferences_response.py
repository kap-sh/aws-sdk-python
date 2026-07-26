"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetConnectionPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.access_type
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_preferences_arn
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.participant_identifier_list
    import capo_partnercentral_account.types.revision


class GetConnectionPreferencesResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "capo_partnercentral_account.types.connection_preferences_arn.ConnectionPreferencesArn"
    """<p>The Amazon Resource Name (ARN) of the connection preferences.</p>"""
    access_type: "capo_partnercentral_account.types.access_type.AccessType"
    """<p>The access type setting for connections (e.g., open, restricted, invitation-only).</p>"""
    excluded_participant_ids: NotRequired[
        "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
    ]
    """<p>A list of participant IDs that are excluded from connection requests or interactions.</p>"""
    updated_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection preferences were last updated.</p>"""
    revision: "capo_partnercentral_account.types.revision.Revision"
    """<p>The revision number of the connection preferences for optimistic locking.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionPreferencesResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    import capo_partnercentral_account.types.access_type

    out["AccessType"] = (
        capo_partnercentral_account.types.access_type.serialize_aws_json_1_0(
            value["access_type"]
        )
    )
    if "excluded_participant_ids" in value:
        import capo_partnercentral_account.types.participant_identifier_list

        out["ExcludedParticipantIds"] = (
            capo_partnercentral_account.types.participant_identifier_list.serialize_aws_json_1_0(
                value["excluded_participant_ids"]
            )
        )
    import capo_partnercentral_account.types.date_time

    out["UpdatedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionPreferencesResponse:
    out: GetConnectionPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetConnectionPreferencesResponse.catalog required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetConnectionPreferencesResponse.arn required")
    if "AccessType" in data:
        import capo_partnercentral_account.types.access_type

        out["access_type"] = (
            capo_partnercentral_account.types.access_type.deserialize_aws_json_1_0(
                data["AccessType"]
            )
        )
    else:
        raise DeserializationError(
            "GetConnectionPreferencesResponse.access_type required"
        )
    if "ExcludedParticipantIds" in data:
        import capo_partnercentral_account.types.participant_identifier_list

        out["excluded_participant_ids"] = (
            capo_partnercentral_account.types.participant_identifier_list.deserialize_aws_json_1_0(
                data["ExcludedParticipantIds"]
            )
        )
    if "UpdatedAt" in data:
        import capo_partnercentral_account.types.date_time

        out["updated_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetConnectionPreferencesResponse.updated_at required"
        )
    if "Revision" in data:
        out["revision"] = data["Revision"]
    else:
        raise DeserializationError("GetConnectionPreferencesResponse.revision required")
    return out
