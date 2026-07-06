"""Generated from Smithy shape ``com.amazonaws.identitystore#Photo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.boolean_type
    import aws_sdk_identitystore.types.sensitive_string_type


class Photo(TypedDict, closed=True):
    value: "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    """<p>The photo data or URL. Supported formats include jpg, jpeg, png, and gif. This field is required for all photo entries.</p>"""
    type: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The type of photo. This field is optional and can be used to categorize different types of photos.</p>"""
    display: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A human-readable description of the photo for display purposes. This optional field provides context about the photo.</p>"""
    primary: "aws_sdk_identitystore.types.boolean_type.BooleanType"
    """<p>Specifies whether this is the user's primary photo. Default value is <code>false</code>. Only one photo can be designated as primary per user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Photo) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    if "type" in value:
        out["Type"] = value["type"]
    if "display" in value:
        out["Display"] = value["display"]
    out["Primary"] = value.get("primary", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> Photo:
    out: Photo = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Photo.value required")
    if "Type" in data:
        out["type"] = data["Type"]
    if "Display" in data:
        out["display"] = data["Display"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    return out
