"""Generated from Smithy shape ``com.amazonaws.inspector2#EcrConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ecr_pull_date_rescan_duration
    import aws_sdk_inspector2.types.ecr_pull_date_rescan_mode
    import aws_sdk_inspector2.types.ecr_rescan_duration


class EcrConfiguration(TypedDict):
    rescan_duration: "aws_sdk_inspector2.types.ecr_rescan_duration.EcrRescanDuration"
    """<p>The rescan duration configured for image push date.</p>"""
    pull_date_rescan_duration: NotRequired[
        "aws_sdk_inspector2.types.ecr_pull_date_rescan_duration.EcrPullDateRescanDuration"
    ]
    """<p>The rescan duration configured for image pull date.</p>"""
    pull_date_rescan_mode: NotRequired[
        "aws_sdk_inspector2.types.ecr_pull_date_rescan_mode.EcrPullDateRescanMode"
    ]
    """<p>The pull date for the re-scan mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrConfiguration) -> dict:
    out: dict = {}
    out["rescanDuration"] = value["rescan_duration"]
    if "pull_date_rescan_duration" in value:
        out["pullDateRescanDuration"] = value["pull_date_rescan_duration"]
    if "pull_date_rescan_mode" in value:
        out["pullDateRescanMode"] = value["pull_date_rescan_mode"]
    return out


def deserialize_json(data: dict) -> EcrConfiguration:
    out: EcrConfiguration = {}  # type: ignore[typeddict-item]
    if "rescanDuration" in data:
        out["rescan_duration"] = data["rescanDuration"]
    else:
        raise DeserializationError("EcrConfiguration.rescan_duration required")
    if "pullDateRescanDuration" in data:
        out["pull_date_rescan_duration"] = data["pullDateRescanDuration"]
    if "pullDateRescanMode" in data:
        out["pull_date_rescan_mode"] = data["pullDateRescanMode"]
    return out
