"""Generated from Smithy shape ``com.amazonaws.evs#DeleteEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_evs.types.environment


class DeleteEnvironmentResponse(TypedDict, closed=True):
    environment: NotRequired["aws_sdk_evs.types.environment.Environment"]
    """<p>A description of the deleted environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentResponse) -> dict:
    out: dict = {}
    if "environment" in value:
        import aws_sdk_evs.types.environment

        out["environment"] = aws_sdk_evs.types.environment.serialize_aws_json_1_0(
            value["environment"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentResponse:
    out: DeleteEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import aws_sdk_evs.types.environment

        out["environment"] = aws_sdk_evs.types.environment.deserialize_aws_json_1_0(
            data["environment"]
        )
    return out
