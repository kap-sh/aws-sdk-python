"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationAssignmentsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn


class ListApplicationAssignmentsFilter(TypedDict):
    application_arn: NotRequired[
        "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    ]
    """<p>The ARN of an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationAssignmentsFilter) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationAssignmentsFilter:
    out: ListApplicationAssignmentsFilter = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    return out
