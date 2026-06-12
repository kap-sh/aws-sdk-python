"""Generated from Smithy shape ``com.amazonaws.comprehend#ListFlywheelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.flywheel_summary_list
    import aws_sdk_comprehend.types.string


class ListFlywheelsResponse(TypedDict):
    flywheel_summary_list: NotRequired[
        "aws_sdk_comprehend.types.flywheel_summary_list.FlywheelSummaryList"
    ]
    """<p>A list of flywheel properties retrieved by the service in response to the request. </p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlywheelsResponse) -> dict:
    out: dict = {}
    if "flywheel_summary_list" in value:
        import aws_sdk_comprehend.types.flywheel_summary_list

        out["FlywheelSummaryList"] = (
            aws_sdk_comprehend.types.flywheel_summary_list.serialize_aws_json_1_1(
                value["flywheel_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlywheelsResponse:
    out: ListFlywheelsResponse = {}  # type: ignore[typeddict-item]
    if "FlywheelSummaryList" in data:
        import aws_sdk_comprehend.types.flywheel_summary_list

        out["flywheel_summary_list"] = (
            aws_sdk_comprehend.types.flywheel_summary_list.deserialize_aws_json_1_1(
                data["FlywheelSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
