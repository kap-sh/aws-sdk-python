"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch_get_profile_id_list
    import aws_sdk_customer_profiles.types.name


class BatchGetProfileRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_ids: "aws_sdk_customer_profiles.types.batch_get_profile_id_list.BatchGetProfileIdList"
    """<p>List of unique identifiers for customer profiles to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetProfileRequest) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.batch_get_profile_id_list

    out["ProfileIds"] = (
        aws_sdk_customer_profiles.types.batch_get_profile_id_list.serialize_json(
            value["profile_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetProfileRequest:
    out: BatchGetProfileRequest = {}  # type: ignore[typeddict-item]
    if "ProfileIds" in data:
        import aws_sdk_customer_profiles.types.batch_get_profile_id_list

        out["profile_ids"] = (
            aws_sdk_customer_profiles.types.batch_get_profile_id_list.deserialize_json(
                data["ProfileIds"]
            )
        )
    else:
        raise DeserializationError("BatchGetProfileRequest.profile_ids required")
    return out
