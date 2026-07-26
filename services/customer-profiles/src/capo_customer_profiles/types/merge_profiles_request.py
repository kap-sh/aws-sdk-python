"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MergeProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.field_source_profile_ids
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.profile_id_to_be_merged_list
    import capo_customer_profiles.types.uuid


class MergeProfilesRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    main_profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The identifier of the profile to be taken.</p>"""
    profile_ids_to_be_merged: "capo_customer_profiles.types.profile_id_to_be_merged_list.ProfileIdToBeMergedList"
    """<p>The identifier of the profile to be merged into MainProfileId.</p>"""
    field_source_profile_ids: NotRequired[
        "capo_customer_profiles.types.field_source_profile_ids.FieldSourceProfileIds"
    ]
    """<p>The identifiers of the fields in the profile that has the information you want to apply to the merge. For example, say you want to merge EmailAddress from Profile1 into MainProfile. This would be the identifier of the EmailAddress field in Profile1. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MergeProfilesRequest) -> dict:
    out: dict = {}
    out["MainProfileId"] = value["main_profile_id"]
    import capo_customer_profiles.types.profile_id_to_be_merged_list

    out["ProfileIdsToBeMerged"] = (
        capo_customer_profiles.types.profile_id_to_be_merged_list.serialize_json(
            value["profile_ids_to_be_merged"]
        )
    )
    if "field_source_profile_ids" in value:
        import capo_customer_profiles.types.field_source_profile_ids

        out["FieldSourceProfileIds"] = (
            capo_customer_profiles.types.field_source_profile_ids.serialize_json(
                value["field_source_profile_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> MergeProfilesRequest:
    out: MergeProfilesRequest = {}  # type: ignore[typeddict-item]
    if "MainProfileId" in data:
        out["main_profile_id"] = data["MainProfileId"]
    else:
        raise DeserializationError("MergeProfilesRequest.main_profile_id required")
    if "ProfileIdsToBeMerged" in data:
        import capo_customer_profiles.types.profile_id_to_be_merged_list

        out["profile_ids_to_be_merged"] = (
            capo_customer_profiles.types.profile_id_to_be_merged_list.deserialize_json(
                data["ProfileIdsToBeMerged"]
            )
        )
    else:
        raise DeserializationError(
            "MergeProfilesRequest.profile_ids_to_be_merged required"
        )
    if "FieldSourceProfileIds" in data:
        import capo_customer_profiles.types.field_source_profile_ids

        out["field_source_profile_ids"] = (
            capo_customer_profiles.types.field_source_profile_ids.deserialize_json(
                data["FieldSourceProfileIds"]
            )
        )
    return out
