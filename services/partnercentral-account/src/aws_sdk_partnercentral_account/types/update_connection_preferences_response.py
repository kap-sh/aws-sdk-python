"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#UpdateConnectionPreferencesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.access_type
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.connection_preferences_arn
    import aws_sdk_partnercentral_account.types.date_time
    import aws_sdk_partnercentral_account.types.participant_identifier_list
    import aws_sdk_partnercentral_account.types.revision


class UpdateConnectionPreferencesResponse(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "aws_sdk_partnercentral_account.types.connection_preferences_arn.ConnectionPreferencesArn"
    """<p>The Amazon Resource Name (ARN) of the updated connection preferences.</p>"""
    access_type: "aws_sdk_partnercentral_account.types.access_type.AccessType"
    """<p>The updated access type setting for connections.</p>"""
    excluded_participant_ids: NotRequired[
        "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
    ]
    """<p>A list of participant IDs that are excluded from connection requests or interactions.</p>"""
    updated_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection preferences were last updated.</p>"""
    revision: "aws_sdk_partnercentral_account.types.revision.Revision"
    """<p>The updated revision number of the connection preferences.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateConnectionPreferencesResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    import aws_sdk_partnercentral_account.types.access_type

    out["AccessType"] = (
        aws_sdk_partnercentral_account.types.access_type.serialize_aws_json_1_0(
            value["access_type"]
        )
    )
    if "excluded_participant_ids" in value:
        import aws_sdk_partnercentral_account.types.participant_identifier_list

        out["ExcludedParticipantIds"] = (
            aws_sdk_partnercentral_account.types.participant_identifier_list.serialize_aws_json_1_0(
                value["excluded_participant_ids"]
            )
        )
    import aws_sdk_partnercentral_account.types.date_time

    out["UpdatedAt"] = (
        aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateConnectionPreferencesResponse:
    out: UpdateConnectionPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "UpdateConnectionPreferencesResponse.catalog required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateConnectionPreferencesResponse.arn required")
    if "AccessType" in data:
        import aws_sdk_partnercentral_account.types.access_type

        out["access_type"] = (
            aws_sdk_partnercentral_account.types.access_type.deserialize_aws_json_1_0(
                data["AccessType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectionPreferencesResponse.access_type required"
        )
    if "ExcludedParticipantIds" in data:
        import aws_sdk_partnercentral_account.types.participant_identifier_list

        out["excluded_participant_ids"] = (
            aws_sdk_partnercentral_account.types.participant_identifier_list.deserialize_aws_json_1_0(
                data["ExcludedParticipantIds"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["updated_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectionPreferencesResponse.updated_at required"
        )
    if "Revision" in data:
        out["revision"] = data["Revision"]
    else:
        raise DeserializationError(
            "UpdateConnectionPreferencesResponse.revision required"
        )
    return out
