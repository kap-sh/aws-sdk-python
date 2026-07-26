"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateAPIKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.api_key


class CreateAPIKeyResponse(TypedDict, closed=True):
    api_key: NotRequired["capo_wafv2.types.api_key.APIKey"]
    """<p>The generated, encrypted API key. You can copy this for use in your JavaScript CAPTCHA integration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAPIKeyResponse) -> dict:
    out: dict = {}
    if "api_key" in value:
        out["APIKey"] = value["api_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAPIKeyResponse:
    out: CreateAPIKeyResponse = {}  # type: ignore[typeddict-item]
    if "APIKey" in data:
        out["api_key"] = data["APIKey"]
    return out
