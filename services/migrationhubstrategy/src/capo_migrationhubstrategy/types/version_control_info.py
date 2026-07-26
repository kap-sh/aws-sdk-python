"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#VersionControlInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.string
    import capo_migrationhubstrategy.types.version_control_type


class VersionControlInfo(TypedDict, closed=True):
    version_control_type: NotRequired[
        "capo_migrationhubstrategy.types.version_control_type.VersionControlType"
    ]
    """<p>The type of version control.</p>"""
    version_control_configuration_time_stamp: NotRequired[
        "capo_migrationhubstrategy.types.string.String"
    ]
    """<p>The time when the version control system was last configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionControlInfo) -> dict:
    out: dict = {}
    if "version_control_type" in value:
        out["versionControlType"] = value["version_control_type"]
    if "version_control_configuration_time_stamp" in value:
        out["versionControlConfigurationTimeStamp"] = value[
            "version_control_configuration_time_stamp"
        ]
    return out


def deserialize_json(data: dict) -> VersionControlInfo:
    out: VersionControlInfo = {}  # type: ignore[typeddict-item]
    if "versionControlType" in data:
        out["version_control_type"] = data["versionControlType"]
    if "versionControlConfigurationTimeStamp" in data:
        out["version_control_configuration_time_stamp"] = data[
            "versionControlConfigurationTimeStamp"
        ]
    return out
