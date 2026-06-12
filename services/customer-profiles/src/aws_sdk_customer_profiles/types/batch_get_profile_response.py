"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch_get_profile_error_list
    import aws_sdk_customer_profiles.types.profile_list


class BatchGetProfileResponse(TypedDict):
    errors: NotRequired[
        "aws_sdk_customer_profiles.types.batch_get_profile_error_list.BatchGetProfileErrorList"
    ]
    """<p>For information about the errors that are common to all actions, see <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/CommonErrors.html\">Common Errors</a>.</p>"""
    profiles: NotRequired["aws_sdk_customer_profiles.types.profile_list.ProfileList"]
    """<p>Array of Profile Objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetProfileResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_customer_profiles.types.batch_get_profile_error_list

        out["Errors"] = (
            aws_sdk_customer_profiles.types.batch_get_profile_error_list.serialize_json(
                value["errors"]
            )
        )
    if "profiles" in value:
        import aws_sdk_customer_profiles.types.profile_list

        out["Profiles"] = aws_sdk_customer_profiles.types.profile_list.serialize_json(
            value["profiles"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetProfileResponse:
    out: BatchGetProfileResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_customer_profiles.types.batch_get_profile_error_list

        out["errors"] = (
            aws_sdk_customer_profiles.types.batch_get_profile_error_list.deserialize_json(
                data["Errors"]
            )
        )
    if "Profiles" in data:
        import aws_sdk_customer_profiles.types.profile_list

        out["profiles"] = aws_sdk_customer_profiles.types.profile_list.deserialize_json(
            data["Profiles"]
        )
    return out
