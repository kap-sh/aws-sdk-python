"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#SourceCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.location
    import capo_migrationhubstrategy.types.project_name
    import capo_migrationhubstrategy.types.source_version
    import capo_migrationhubstrategy.types.version_control


class SourceCode(TypedDict, closed=True):
    version_control: NotRequired[
        "capo_migrationhubstrategy.types.version_control.VersionControl"
    ]
    """<p> The type of repository to use for the source code. </p>"""
    source_version: NotRequired[
        "capo_migrationhubstrategy.types.source_version.SourceVersion"
    ]
    """<p> The branch of the source code. </p>"""
    location: NotRequired["capo_migrationhubstrategy.types.location.Location"]
    """<p> The repository name for the source code. </p>"""
    project_name: NotRequired[
        "capo_migrationhubstrategy.types.project_name.ProjectName"
    ]
    """<p>The name of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceCode) -> dict:
    out: dict = {}
    if "version_control" in value:
        out["versionControl"] = value["version_control"]
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "location" in value:
        out["location"] = value["location"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    return out


def deserialize_json(data: dict) -> SourceCode:
    out: SourceCode = {}  # type: ignore[typeddict-item]
    if "versionControl" in data:
        out["version_control"] = data["versionControl"]
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    if "location" in data:
        out["location"] = data["location"]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    return out
