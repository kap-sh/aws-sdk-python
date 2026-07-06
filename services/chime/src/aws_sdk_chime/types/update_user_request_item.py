"""Generated from Smithy shape ``com.amazonaws.chime#UpdateUserRequestItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.alexa_for_business_metadata
    import aws_sdk_chime.types.license
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.user_type


class UpdateUserRequestItem(TypedDict, closed=True):
    user_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The user ID.</p>"""
    license_type: NotRequired["aws_sdk_chime.types.license.License"]
    """<p>The user license type.</p>"""
    user_type: NotRequired["aws_sdk_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""
    alexa_for_business_metadata: NotRequired[
        "aws_sdk_chime.types.alexa_for_business_metadata.AlexaForBusinessMetadata"
    ]
    """<p>The Alexa for Business metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequestItem) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    if "license_type" in value:
        import aws_sdk_chime.types.license

        out["LicenseType"] = aws_sdk_chime.types.license.serialize_json(
            value["license_type"]
        )
    if "user_type" in value:
        import aws_sdk_chime.types.user_type

        out["UserType"] = aws_sdk_chime.types.user_type.serialize_json(
            value["user_type"]
        )
    if "alexa_for_business_metadata" in value:
        import aws_sdk_chime.types.alexa_for_business_metadata

        out["AlexaForBusinessMetadata"] = (
            aws_sdk_chime.types.alexa_for_business_metadata.serialize_json(
                value["alexa_for_business_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateUserRequestItem:
    out: UpdateUserRequestItem = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("UpdateUserRequestItem.user_id required")
    if "LicenseType" in data:
        import aws_sdk_chime.types.license

        out["license_type"] = aws_sdk_chime.types.license.deserialize_json(
            data["LicenseType"]
        )
    if "UserType" in data:
        import aws_sdk_chime.types.user_type

        out["user_type"] = aws_sdk_chime.types.user_type.deserialize_json(
            data["UserType"]
        )
    if "AlexaForBusinessMetadata" in data:
        import aws_sdk_chime.types.alexa_for_business_metadata

        out["alexa_for_business_metadata"] = (
            aws_sdk_chime.types.alexa_for_business_metadata.deserialize_json(
                data["AlexaForBusinessMetadata"]
            )
        )
    return out
