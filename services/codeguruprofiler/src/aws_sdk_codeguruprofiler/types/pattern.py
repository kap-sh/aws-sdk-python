"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Pattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.percentage
    import aws_sdk_codeguruprofiler.types.strings
    import aws_sdk_codeguruprofiler.types.target_frames


class Pattern(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The universally unique identifier (UUID) of this pattern.</p>"""
    name: NotRequired["str"]
    """<p>The name for this pattern.</p>"""
    description: NotRequired["str"]
    """<p>The description of the recommendation. This explains a potential inefficiency in a profiled application.</p>"""
    resolution_steps: NotRequired["str"]
    """<p> A string that contains the steps recommended to address the potential inefficiency. </p>"""
    target_frames: NotRequired[
        "aws_sdk_codeguruprofiler.types.target_frames.TargetFrames"
    ]
    """<p>A list of frame names that were searched during the analysis that generated a recommendation.</p>"""
    threshold_percent: "aws_sdk_codeguruprofiler.types.percentage.Percentage"
    """<p> The percentage of time an application spends in one method that triggers a recommendation. The percentage of time is the same as the percentage of the total gathered sample counts during analysis. </p>"""
    counters_to_aggregate: NotRequired["aws_sdk_codeguruprofiler.types.strings.Strings"]
    """<p> A list of the different counters used to determine if there is a match. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Pattern) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "resolution_steps" in value:
        out["resolutionSteps"] = value["resolution_steps"]
    if "target_frames" in value:
        import aws_sdk_codeguruprofiler.types.target_frames

        out["targetFrames"] = (
            aws_sdk_codeguruprofiler.types.target_frames.serialize_json(
                value["target_frames"]
            )
        )
    out["thresholdPercent"] = value.get("threshold_percent", 0)
    if "counters_to_aggregate" in value:
        import aws_sdk_codeguruprofiler.types.strings

        out["countersToAggregate"] = (
            aws_sdk_codeguruprofiler.types.strings.serialize_json(
                value["counters_to_aggregate"]
            )
        )
    return out


def deserialize_json(data: dict) -> Pattern:
    out: Pattern = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "resolutionSteps" in data:
        out["resolution_steps"] = data["resolutionSteps"]
    if "targetFrames" in data:
        import aws_sdk_codeguruprofiler.types.target_frames

        out["target_frames"] = (
            aws_sdk_codeguruprofiler.types.target_frames.deserialize_json(
                data["targetFrames"]
            )
        )
    if "thresholdPercent" in data:
        out["threshold_percent"] = data["thresholdPercent"]
    else:
        out["threshold_percent"] = 0
    if "countersToAggregate" in data:
        import aws_sdk_codeguruprofiler.types.strings

        out["counters_to_aggregate"] = (
            aws_sdk_codeguruprofiler.types.strings.deserialize_json(
                data["countersToAggregate"]
            )
        )
    return out
