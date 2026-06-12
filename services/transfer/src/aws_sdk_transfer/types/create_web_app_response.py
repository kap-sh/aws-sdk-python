"""Generated from Smithy shape ``com.amazonaws.transfer#CreateWebAppResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.web_app_id


class CreateWebAppResponse(TypedDict):
    web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId"
    """<p>Returns a unique identifier for the web app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebAppResponse) -> dict:
    out: dict = {}
    out["WebAppId"] = value["web_app_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebAppResponse:
    out: CreateWebAppResponse = {}  # type: ignore[typeddict-item]
    if "WebAppId" in data:
        out["web_app_id"] = data["WebAppId"]
    else:
        raise DeserializationError("CreateWebAppResponse.web_app_id required")
    return out
