"""Generated from Smithy shape ``com.amazonaws.interconnect#GetEnvironmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.environment


class GetEnvironmentResponse(TypedDict):
    environment: "aws_sdk_interconnect.types.environment.Environment"
    """<p>The requested <a>Environment</a> structure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentResponse) -> dict:
    out: dict = {}
    import aws_sdk_interconnect.types.environment

    out["environment"] = aws_sdk_interconnect.types.environment.serialize_aws_json_1_0(
        value["environment"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentResponse:
    out: GetEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_interconnect.types.environment

        out["environment"] = (
            aws_sdk_interconnect.types.environment.deserialize_aws_json_1_0(
                data["environment"]
            )
        )
    else:
        raise DeserializationError("GetEnvironmentResponse.environment required")
    return out
