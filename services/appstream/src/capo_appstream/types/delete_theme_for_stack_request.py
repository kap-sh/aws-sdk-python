"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteThemeForStackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.name


class DeleteThemeForStackRequest(TypedDict, closed=True):
    stack_name: NotRequired["capo_appstream.types.name.Name"]
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
