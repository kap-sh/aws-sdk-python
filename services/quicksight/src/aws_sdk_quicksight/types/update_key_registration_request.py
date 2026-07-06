"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateKeyRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.key_registration


class UpdateKeyRegistrationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the customer managed key registration that you want to update.</p>"""
    key_registration: "aws_sdk_quicksight.types.key_registration.KeyRegistration"
    """<p>A list of <code>RegisteredCustomerManagedKey</code> objects to be updated to the Quick Sight account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKeyRegistrationRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.key_registration

    out["KeyRegistration"] = aws_sdk_quicksight.types.key_registration.serialize_json(
        value["key_registration"]
    )
    return out


def deserialize_json(data: dict) -> UpdateKeyRegistrationRequest:
    out: UpdateKeyRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "KeyRegistration" in data:
        import aws_sdk_quicksight.types.key_registration

        out["key_registration"] = (
            aws_sdk_quicksight.types.key_registration.deserialize_json(
                data["KeyRegistration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateKeyRegistrationRequest.key_registration required"
        )
    return out
