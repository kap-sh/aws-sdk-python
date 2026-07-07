"""Generated from Smithy shape ``com.amazonaws.evs#GetEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_evs.types.environment


class GetEnvironmentResponse(TypedDict, closed=True):
    environment: NotRequired["aws_sdk_evs.types.environment.Environment"]
    """<p>A description of the requested environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment" in value:
        import aws_sdk_evs.types.environment

        out["environment"] = aws_sdk_evs.types.environment.serialize_aws_json_1_0(
            value["environment"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentResponse:
    out: GetEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_evs.types.environment

        out["environment"] = aws_sdk_evs.types.environment.deserialize_aws_json_1_0(
            data["environment"]
        )
    return out
