"""Generated from Smithy shape ``com.amazonaws.securityhub#JiraCloudUpdateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class JiraCloudUpdateConfiguration(TypedDict, closed=True):
    project_key: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The project key for a JiraCloud instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraCloudUpdateConfiguration) -> dict:
    out: dict = {}
    if "project_key" in value:
        out["ProjectKey"] = value["project_key"]
    return out


def deserialize_json(data: dict) -> JiraCloudUpdateConfiguration:
    out: JiraCloudUpdateConfiguration = {}  # type: ignore[typeddict-item]
    if "ProjectKey" in data:
        out["project_key"] = data["ProjectKey"]
    return out
