"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteThemeForStackRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.name


class DeleteThemeForStackRequest(TypedDict):
    stack_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the stack for the theme.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteThemeForStackRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteThemeForStackRequest:
    out: DeleteThemeForStackRequest = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    return out
