"""Generated from Smithy shape ``com.amazonaws.appsync#CreateApiResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api


class CreateApiResponse(TypedDict):
    api: NotRequired["aws_sdk_appsync.types.api.Api"]
    """<p>The <code>Api</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiResponse) -> dict:
    out: dict = {}
    if "api" in value:
        import aws_sdk_appsync.types.api

        out["api"] = aws_sdk_appsync.types.api.serialize_json(value["api"])
    return out


def deserialize_json(data: dict) -> CreateApiResponse:
    out: CreateApiResponse = {}  # type: ignore[typeddict-item]
    if "api" in data:
        import aws_sdk_appsync.types.api

        out["api"] = aws_sdk_appsync.types.api.deserialize_json(data["api"])
    return out
