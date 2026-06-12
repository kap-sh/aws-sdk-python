"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectBadge``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.boolean
    import aws_sdk_codebuild.types.string


class ProjectBadge(TypedDict):
    badge_enabled: "aws_sdk_codebuild.types.boolean.Boolean"
    """<p>Set this to true to generate a publicly accessible URL for your project's build badge.</p>"""
    badge_request_url: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The publicly-accessible URL through which you can access the build badge for your project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectBadge) -> dict:
    out: dict = {}
    out["badgeEnabled"] = value.get("badge_enabled", False)
    if "badge_request_url" in value:
        out["badgeRequestUrl"] = value["badge_request_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectBadge:
    out: ProjectBadge = {}  # type: ignore[typeddict-item]
    if "badgeEnabled" in data:
        out["badge_enabled"] = data["badgeEnabled"]
    else:
        out["badge_enabled"] = False
    if "badgeRequestUrl" in data:
        out["badge_request_url"] = data["badgeRequestUrl"]
    return out
