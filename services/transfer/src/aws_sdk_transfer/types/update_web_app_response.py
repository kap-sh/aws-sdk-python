"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.web_app_id


class UpdateWebAppResponse(TypedDict):
    web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId"
    """<p>Returns the unique identifier for the web app being updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppResponse) -> dict:
    out: dict = {}
    out["WebAppId"] = value["web_app_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppResponse:
    out: UpdateWebAppResponse = {}  # type: ignore[typeddict-item]
    if "WebAppId" in data:
        out["web_app_id"] = data["WebAppId"]
    else:
        raise DeserializationError("UpdateWebAppResponse.web_app_id required")
    return out
