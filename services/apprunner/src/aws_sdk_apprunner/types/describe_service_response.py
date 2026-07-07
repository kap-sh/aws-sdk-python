"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.service


class DescribeServiceResponse(TypedDict, closed=True):
    service: "aws_sdk_apprunner.types.service.Service"
    """<p>A full description of the App Runner service that you specified in this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeServiceResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.service

    out["Service"] = aws_sdk_apprunner.types.service.serialize_aws_json_1_0(
        value["service"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeServiceResponse:
    out: DescribeServiceResponse = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        import aws_sdk_apprunner.types.service

        out["service"] = aws_sdk_apprunner.types.service.deserialize_aws_json_1_0(
            data["Service"]
        )
    else:
        raise DeserializationError("DescribeServiceResponse.service required")
    return out
