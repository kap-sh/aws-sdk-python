"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CompositionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.composition_arn
    import aws_sdk_ivs_realtime.types.composition_state
    import aws_sdk_ivs_realtime.types.destination_summary_list
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.tags
    import aws_sdk_ivs_realtime.types.time


class CompositionSummary(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.composition_arn.CompositionArn"
    """<p>ARN of the Composition resource.</p>"""
    stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the attached stage.</p>"""
    destinations: (
        "aws_sdk_ivs_realtime.types.destination_summary_list.DestinationSummaryList"
    )
    """<p>Array of Destination objects.</p>"""
    state: "aws_sdk_ivs_realtime.types.composition_state.CompositionState"
    """<p>State of the Composition resource.</p>"""
    tags: NotRequired["aws_sdk_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""
    start_time: NotRequired["aws_sdk_ivs_realtime.types.time.Time"]
    """<p>UTC time of the Composition start. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""
    end_time: NotRequired["aws_sdk_ivs_realtime.types.time.Time"]
    """<p>UTC time of the Composition end. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositionSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["stageArn"] = value["stage_arn"]
    import aws_sdk_ivs_realtime.types.destination_summary_list

    out["destinations"] = (
        aws_sdk_ivs_realtime.types.destination_summary_list.serialize_json(
            value["destinations"]
        )
    )
    out["state"] = value["state"]
    if "tags" in value:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.serialize_json(value["tags"])
    if "start_time" in value:
        import aws_sdk_ivs_realtime.types.time

        out["startTime"] = aws_sdk_ivs_realtime.types.time.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ivs_realtime.types.time

        out["endTime"] = aws_sdk_ivs_realtime.types.time.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> CompositionSummary:
    out: CompositionSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CompositionSummary.arn required")
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("CompositionSummary.stage_arn required")
    if "destinations" in data:
        import aws_sdk_ivs_realtime.types.destination_summary_list

        out["destinations"] = (
            aws_sdk_ivs_realtime.types.destination_summary_list.deserialize_json(
                data["destinations"]
            )
        )
    else:
        raise DeserializationError("CompositionSummary.destinations required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("CompositionSummary.state required")
    if "tags" in data:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.deserialize_json(data["tags"])
    if "startTime" in data:
        import aws_sdk_ivs_realtime.types.time

        out["start_time"] = aws_sdk_ivs_realtime.types.time.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_ivs_realtime.types.time

        out["end_time"] = aws_sdk_ivs_realtime.types.time.deserialize_json(
            data["endTime"]
        )
    return out
