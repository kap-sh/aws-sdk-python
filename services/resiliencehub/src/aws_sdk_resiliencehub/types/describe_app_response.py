"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app


class DescribeAppResponse(TypedDict):
    app: "aws_sdk_resiliencehub.types.app.App"
    """<p>The specified application, returned as an object with details including compliance status, creation time, description, resiliency score, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.app

    out["app"] = aws_sdk_resiliencehub.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> DescribeAppResponse:
    out: DescribeAppResponse = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import aws_sdk_resiliencehub.types.app

        out["app"] = aws_sdk_resiliencehub.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("DescribeAppResponse.app required")
    return out
