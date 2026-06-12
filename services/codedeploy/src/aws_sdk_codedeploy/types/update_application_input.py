"""Generated from Smithy shape ``com.amazonaws.codedeploy#UpdateApplicationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name


class UpdateApplicationInput(TypedDict):
    application_name: NotRequired[
        "aws_sdk_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The current name of the application you want to change.</p>"""
    new_application_name: NotRequired[
        "aws_sdk_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The new name to give the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationInput) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "new_application_name" in value:
        out["newApplicationName"] = value["new_application_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationInput:
    out: UpdateApplicationInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "newApplicationName" in data:
        out["new_application_name"] = data["newApplicationName"]
    return out
