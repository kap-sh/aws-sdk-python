"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#UpdateConnectionPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.access_type
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.participant_identifier_list
    import aws_sdk_partnercentral_account.types.revision


class UpdateConnectionPreferencesRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    revision: "aws_sdk_partnercentral_account.types.revision.Revision"
    """<p>The revision number of the connection preferences for optimistic locking.</p>"""
    access_type: "aws_sdk_partnercentral_account.types.access_type.AccessType"
    """<p>The access type setting for connections (e.g., open, restricted, invitation-only).</p>"""
    excluded_participant_identifiers: NotRequired[
        "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
    ]
    """<p>The updated list of participant identifiers to exclude from connections.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateConnectionPreferencesRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Revision"] = value["revision"]
    import aws_sdk_partnercentral_account.types.access_type

    out["AccessType"] = (
        aws_sdk_partnercentral_account.types.access_type.serialize_aws_json_1_0(
            value["access_type"]
        )
    )
    if "excluded_participant_identifiers" in value:
        import aws_sdk_partnercentral_account.types.participant_identifier_list

        out["ExcludedParticipantIdentifiers"] = (
            aws_sdk_partnercentral_account.types.participant_identifier_list.serialize_aws_json_1_0(
                value["excluded_participant_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateConnectionPreferencesRequest:
    out: UpdateConnectionPreferencesRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "UpdateConnectionPreferencesRequest.catalog required"
        )
    if "Revision" in data:
        out["revision"] = data["Revision"]
    else:
        raise DeserializationError(
            "UpdateConnectionPreferencesRequest.revision required"
        )
    if "AccessType" in data:
        import aws_sdk_partnercentral_account.types.access_type

        out["access_type"] = (
            aws_sdk_partnercentral_account.types.access_type.deserialize_aws_json_1_0(
                data["AccessType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectionPreferencesRequest.access_type required"
        )
    if "ExcludedParticipantIdentifiers" in data:
        import aws_sdk_partnercentral_account.types.participant_identifier_list

        out["excluded_participant_identifiers"] = (
            aws_sdk_partnercentral_account.types.participant_identifier_list.deserialize_aws_json_1_0(
                data["ExcludedParticipantIdentifiers"]
            )
        )
    return out
