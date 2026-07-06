"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#HttpHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type


class HttpHeader(TypedDict, closed=True):
    header_name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The header name.</p>"""
    header_value: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The header value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpHeader) -> dict:
    out: dict = {}
    if "header_name" in value:
        out["headerName"] = value["header_name"]
    if "header_value" in value:
        out["headerValue"] = value["header_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpHeader:
    out: HttpHeader = {}  # type: ignore[typeddict-item]
    if "headerName" in data:
        out["header_name"] = data["headerName"]
    if "headerValue" in data:
        out["header_value"] = data["headerValue"]
    return out
