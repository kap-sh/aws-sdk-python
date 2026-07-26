"""Generated from Smithy shape ``com.amazonaws.macie2#GetSensitiveDataOccurrencesAvailabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_unavailability_reason_code
    import capo_macie2.types.availability_code


class GetSensitiveDataOccurrencesAvailabilityResponse(TypedDict, closed=True):
    code: NotRequired["capo_macie2.types.availability_code.AvailabilityCode"]
    """<p>Specifies whether occurrences of sensitive data can be retrieved for the finding. Possible values are: AVAILABLE, the sensitive data can be retrieved; and, UNAVAILABLE, the sensitive data can't be retrieved. If this value is UNAVAILABLE, the reasons array indicates why the data can't be retrieved.</p>"""
    reasons: NotRequired[
        "capo_macie2.types.__list_of_unavailability_reason_code.__listOfUnavailabilityReasonCode"
    ]
    """<p>Specifies why occurrences of sensitive data can't be retrieved for the finding. Possible values are:</p> <ul><li><p>ACCOUNT_NOT_IN_ORGANIZATION - The affected account isn't currently part of your organization. Or the account is part of your organization but Macie isn't currently enabled for the account. You're not allowed to access the affected S3 object by using Macie.</p></li> <li><p>INVALID_CLASSIFICATION_RESULT - There isn't a corresponding sensitive data discovery result for the finding. Or the corresponding sensitive data discovery result isn't available in the current Amazon Web Services Region, is malformed or corrupted, or uses an unsupported storage format. Macie can't verify the location of the sensitive data to retrieve.</p></li> <li><p>INVALID_RESULT_SIGNATURE - The corresponding sensitive data discovery result is stored in an S3 object that wasn't signed by Macie. Macie can't verify the integrity and authenticity of the sensitive data discovery result. Therefore, Macie can't verify the location of the sensitive data to retrieve.</p></li> <li><p>MEMBER_ROLE_TOO_PERMISSIVE - The trust or permissions policy for the IAM role in the affected member account doesn't meet Macie requirements for restricting access to the role. Or the role's trust policy doesn't specify the correct external ID for your organization. Macie can't assume the role to retrieve the sensitive data.</p></li> <li><p>MISSING_GET_MEMBER_PERMISSION - You're not allowed to retrieve information about the association between your account and the affected account. Macie can't determine whether you’re allowed to access the affected S3 object as the delegated Macie administrator for the affected account.</p></li> <li><p>OBJECT_EXCEEDS_SIZE_QUOTA - The storage size of the affected S3 object exceeds the size quota for retrieving occurrences of sensitive data from this type of file.</p></li> <li><p>OBJECT_UNAVAILABLE - The affected S3 object isn't available. The object was renamed, moved, deleted, or changed after Macie created the finding. Or the object is encrypted with an KMS key that isn’t available. For example, the key is disabled, is scheduled for deletion, or was deleted.</p></li> <li><p>RESULT_NOT_SIGNED - The corresponding sensitive data discovery result is stored in an S3 object that hasn't been signed. Macie can't verify the integrity and authenticity of the sensitive data discovery result. Therefore, Macie can't verify the location of the sensitive data to retrieve.</p></li> <li><p>ROLE_TOO_PERMISSIVE - Your account is configured to retrieve occurrences of sensitive data by using an IAM role whose trust or permissions policy doesn't meet Macie requirements for restricting access to the role. Macie can’t assume the role to retrieve the sensitive data.</p></li> <li><p>UNSUPPORTED_FINDING_TYPE - The specified finding isn't a sensitive data finding.</p></li> <li><p>UNSUPPORTED_OBJECT_TYPE - The affected S3 object uses a file or storage format that Macie doesn't support for retrieving occurrences of sensitive data.</p></li></ul> <p>This value is null if sensitive data can be retrieved for the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSensitiveDataOccurrencesAvailabilityResponse) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_macie2.types.availability_code

        out["code"] = capo_macie2.types.availability_code.serialize_json(value["code"])
    if "reasons" in value:
        import capo_macie2.types.__list_of_unavailability_reason_code

        out["reasons"] = (
            capo_macie2.types.__list_of_unavailability_reason_code.serialize_json(
                value["reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSensitiveDataOccurrencesAvailabilityResponse:
    out: GetSensitiveDataOccurrencesAvailabilityResponse = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import capo_macie2.types.availability_code

        out["code"] = capo_macie2.types.availability_code.deserialize_json(data["code"])
    if "reasons" in data:
        import capo_macie2.types.__list_of_unavailability_reason_code

        out["reasons"] = (
            capo_macie2.types.__list_of_unavailability_reason_code.deserialize_json(
                data["reasons"]
            )
        )
    return out
