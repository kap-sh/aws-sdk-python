"""Generated from Smithy shape ``com.amazonaws.connect#UpdateWorkspaceThemeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.workspace_id
    import aws_sdk_connect.types.workspace_theme


class UpdateWorkspaceThemeRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "aws_sdk_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    theme: NotRequired["aws_sdk_connect.types.workspace_theme.WorkspaceTheme"]
    """<p>The theme configuration, including color schemes and visual styles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceThemeRequest) -> dict:
    out: dict = {}
    if "theme" in value:
        import aws_sdk_connect.types.workspace_theme

        out["Theme"] = aws_sdk_connect.types.workspace_theme.serialize_json(
            value["theme"]
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceThemeRequest:
    out: UpdateWorkspaceThemeRequest = {}  # type: ignore[typeddict-item]
    if "Theme" in data:
        import aws_sdk_connect.types.workspace_theme

        out["theme"] = aws_sdk_connect.types.workspace_theme.deserialize_json(
            data["Theme"]
        )
    return out
