"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateProblemRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.problem_id
    import aws_sdk_application_insights.types.update_status
    import aws_sdk_application_insights.types.visibility


class UpdateProblemRequest(TypedDict):
    problem_id: "aws_sdk_application_insights.types.problem_id.ProblemId"
    """<p>The ID of the problem.</p>"""
    update_status: NotRequired[
        "aws_sdk_application_insights.types.update_status.UpdateStatus"
    ]
    """<p>The status of the problem. Arguments can be passed for only problems that show a status of <code>RECOVERING</code>.</p>"""
    visibility: NotRequired["aws_sdk_application_insights.types.visibility.Visibility"]
    """<p>The visibility of a problem. When you pass a value of <code>IGNORED</code>, the problem is removed from the default view, and all notifications for the problem are suspended. When <code>VISIBLE</code> is passed, the <code>IGNORED</code> action is reversed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProblemRequest) -> dict:
    out: dict = {}
    out["ProblemId"] = value["problem_id"]
    if "update_status" in value:
        import aws_sdk_application_insights.types.update_status

        out["UpdateStatus"] = (
            aws_sdk_application_insights.types.update_status.serialize_aws_json_1_1(
                value["update_status"]
            )
        )
    if "visibility" in value:
        import aws_sdk_application_insights.types.visibility

        out["Visibility"] = (
            aws_sdk_application_insights.types.visibility.serialize_aws_json_1_1(
                value["visibility"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProblemRequest:
    out: UpdateProblemRequest = {}  # type: ignore[typeddict-item]
    if "ProblemId" in data:
        out["problem_id"] = data["ProblemId"]
    else:
        raise DeserializationError("UpdateProblemRequest.problem_id required")
    if "UpdateStatus" in data:
        import aws_sdk_application_insights.types.update_status

        out["update_status"] = (
            aws_sdk_application_insights.types.update_status.deserialize_aws_json_1_1(
                data["UpdateStatus"]
            )
        )
    if "Visibility" in data:
        import aws_sdk_application_insights.types.visibility

        out["visibility"] = (
            aws_sdk_application_insights.types.visibility.deserialize_aws_json_1_1(
                data["Visibility"]
            )
        )
    return out
