"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#IssueDetectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.rule_name


class IssueDetectionConfiguration(TypedDict, closed=True):
    rule_name: "capo_chime_sdk_media_pipelines.types.rule_name.RuleName"
    """<p>The name of the issue detection rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IssueDetectionConfiguration) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    return out


def deserialize_json(data: dict) -> IssueDetectionConfiguration:
    out: IssueDetectionConfiguration = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError("IssueDetectionConfiguration.rule_name required")
    return out
