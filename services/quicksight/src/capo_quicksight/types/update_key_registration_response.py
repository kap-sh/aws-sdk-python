"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateKeyRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.failed_key_registration_entries
    import capo_quicksight.types.non_empty_string
    import capo_quicksight.types.successful_key_registration_entries


class UpdateKeyRegistrationResponse(TypedDict, closed=True):
    failed_key_registration: NotRequired[
        "capo_quicksight.types.failed_key_registration_entries.FailedKeyRegistrationEntries"
    ]
    """<p>A list of all customer managed key registrations that failed to update.</p>"""
    successful_key_registration: NotRequired[
        "capo_quicksight.types.successful_key_registration_entries.SuccessfulKeyRegistrationEntries"
    ]
    """<p>A list of all customer managed key registrations that were successfully updated.</p>"""
    request_id: NotRequired["capo_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKeyRegistrationResponse) -> dict:
    out: dict = {}
    if "failed_key_registration" in value:
        import capo_quicksight.types.failed_key_registration_entries

        out["FailedKeyRegistration"] = (
            capo_quicksight.types.failed_key_registration_entries.serialize_json(
                value["failed_key_registration"]
            )
        )
    if "successful_key_registration" in value:
        import capo_quicksight.types.successful_key_registration_entries

        out["SuccessfulKeyRegistration"] = (
            capo_quicksight.types.successful_key_registration_entries.serialize_json(
                value["successful_key_registration"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateKeyRegistrationResponse:
    out: UpdateKeyRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "FailedKeyRegistration" in data:
        import capo_quicksight.types.failed_key_registration_entries

        out["failed_key_registration"] = (
            capo_quicksight.types.failed_key_registration_entries.deserialize_json(
                data["FailedKeyRegistration"]
            )
        )
    if "SuccessfulKeyRegistration" in data:
        import capo_quicksight.types.successful_key_registration_entries

        out["successful_key_registration"] = (
            capo_quicksight.types.successful_key_registration_entries.deserialize_json(
                data["SuccessfulKeyRegistration"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
