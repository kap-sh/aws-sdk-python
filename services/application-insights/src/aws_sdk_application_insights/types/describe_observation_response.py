"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeObservationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.observation


class DescribeObservationResponse(TypedDict):
    observation: NotRequired[
        "aws_sdk_application_insights.types.observation.Observation"
    ]
    """<p>Information about the observation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeObservationResponse) -> dict:
    out: dict = {}
    if "observation" in value:
        import aws_sdk_application_insights.types.observation

        out["Observation"] = (
            aws_sdk_application_insights.types.observation.serialize_aws_json_1_1(
                value["observation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeObservationResponse:
    out: DescribeObservationResponse = {}  # type: ignore[typeddict-item]
    if "Observation" in data:
        import aws_sdk_application_insights.types.observation

        out["observation"] = (
            aws_sdk_application_insights.types.observation.deserialize_aws_json_1_1(
                data["Observation"]
            )
        )
    return out
