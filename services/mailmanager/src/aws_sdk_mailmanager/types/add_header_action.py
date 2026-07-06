"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddHeaderAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.header_name
    import aws_sdk_mailmanager.types.header_value


class AddHeaderAction(TypedDict, closed=True):
    header_name: "aws_sdk_mailmanager.types.header_name.HeaderName"
    r"""<p>The name of the header to add to an email. The header must be prefixed with \"X-\". Headers are added regardless of whether the header name pre-existed in the email.</p>"""
    header_value: "aws_sdk_mailmanager.types.header_value.HeaderValue"
    """<p>The value of the header to add to the email.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddHeaderAction) -> dict:
    out: dict = {}
    out["HeaderName"] = value["header_name"]
    out["HeaderValue"] = value["header_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AddHeaderAction:
    out: AddHeaderAction = {}  # type: ignore[typeddict-item]
    if "HeaderName" in data:
        out["header_name"] = data["HeaderName"]
    else:
        raise DeserializationError("AddHeaderAction.header_name required")
    if "HeaderValue" in data:
        out["header_value"] = data["HeaderValue"]
    else:
        raise DeserializationError("AddHeaderAction.header_value required")
    return out
