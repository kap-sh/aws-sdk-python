"""Generated from Smithy shape ``com.amazonaws.transfer#CustomHttpHeader``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.custom_http_header_key_type
    import aws_sdk_transfer.types.custom_http_header_value_type


class CustomHttpHeader(TypedDict):
    key: NotRequired[
        "aws_sdk_transfer.types.custom_http_header_key_type.CustomHttpHeaderKeyType"
    ]
    """<p>The name of the custom HTTP header.</p>"""
    value: NotRequired[
        "aws_sdk_transfer.types.custom_http_header_value_type.CustomHttpHeaderValueType"
    ]
    """<p>The value of the custom HTTP header.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomHttpHeader) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomHttpHeader:
    out: CustomHttpHeader = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
