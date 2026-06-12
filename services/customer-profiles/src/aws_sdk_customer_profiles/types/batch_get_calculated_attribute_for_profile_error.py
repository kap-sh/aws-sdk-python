"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetCalculatedAttributeForProfileError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.string1_to1000
    import aws_sdk_customer_profiles.types.uuid


class BatchGetCalculatedAttributeForProfileError(TypedDict):
    code: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>Status code for why a specific profile and calculated attribute failed.</p>"""
    message: "aws_sdk_customer_profiles.types.string1_to1000.string1To1000"
    """<p>Message describing why a specific profile and calculated attribute failed.</p>"""
    profile_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The profile id that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCalculatedAttributeForProfileError) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    out["Message"] = value["message"]
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_json(data: dict) -> BatchGetCalculatedAttributeForProfileError:
    out: BatchGetCalculatedAttributeForProfileError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError(
            "BatchGetCalculatedAttributeForProfileError.code required"
        )
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError(
            "BatchGetCalculatedAttributeForProfileError.message required"
        )
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError(
            "BatchGetCalculatedAttributeForProfileError.profile_id required"
        )
    return out
