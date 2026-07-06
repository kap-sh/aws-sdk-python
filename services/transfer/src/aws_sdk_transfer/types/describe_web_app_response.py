"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeWebAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_web_app


class DescribeWebAppResponse(TypedDict, closed=True):
    web_app: "aws_sdk_transfer.types.described_web_app.DescribedWebApp"
    """<p>Returns a structure that contains the details of the web app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWebAppResponse) -> dict:
    out: dict = {}
    import aws_sdk_transfer.types.described_web_app

    out["WebApp"] = aws_sdk_transfer.types.described_web_app.serialize_aws_json_1_1(
        value["web_app"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWebAppResponse:
    out: DescribeWebAppResponse = {}  # type: ignore[typeddict-item]
    if "WebApp" in data:
        import aws_sdk_transfer.types.described_web_app

        out["web_app"] = (
            aws_sdk_transfer.types.described_web_app.deserialize_aws_json_1_1(
                data["WebApp"]
            )
        )
    else:
        raise DeserializationError("DescribeWebAppResponse.web_app required")
    return out
