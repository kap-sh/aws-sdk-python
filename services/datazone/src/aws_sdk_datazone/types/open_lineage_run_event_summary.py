"""Generated from Smithy shape ``com.amazonaws.datazone#OpenLineageRunEventSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.name_identifier
    import aws_sdk_datazone.types.name_identifiers
    import aws_sdk_datazone.types.open_lineage_run_state


class OpenLineageRunEventSummary(TypedDict):
    event_type: NotRequired[
        "aws_sdk_datazone.types.open_lineage_run_state.OpenLineageRunState"
    ]
    """<p>The event type of the open lineage run event summary.</p>"""
    run_id: NotRequired["str"]
    """<p>The runID of the open lineage run event summary.</p>"""
    job: NotRequired["aws_sdk_datazone.types.name_identifier.NameIdentifier"]
    """<p>The job of the open lineage run event summary.</p>"""
    inputs: NotRequired["aws_sdk_datazone.types.name_identifiers.NameIdentifiers"]
    """<p>The inputs of the open lineage run event summary.</p>"""
    outputs: NotRequired["aws_sdk_datazone.types.name_identifiers.NameIdentifiers"]
    """<p>The outputs of the open lineage run event summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenLineageRunEventSummary) -> dict:
    out: dict = {}
    if "event_type" in value:
        import aws_sdk_datazone.types.open_lineage_run_state

        out["eventType"] = aws_sdk_datazone.types.open_lineage_run_state.serialize_json(
            value["event_type"]
        )
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "job" in value:
        import aws_sdk_datazone.types.name_identifier

        out["job"] = aws_sdk_datazone.types.name_identifier.serialize_json(value["job"])
    if "inputs" in value:
        import aws_sdk_datazone.types.name_identifiers

        out["inputs"] = aws_sdk_datazone.types.name_identifiers.serialize_json(
            value["inputs"]
        )
    if "outputs" in value:
        import aws_sdk_datazone.types.name_identifiers

        out["outputs"] = aws_sdk_datazone.types.name_identifiers.serialize_json(
            value["outputs"]
        )
    return out


def deserialize_json(data: dict) -> OpenLineageRunEventSummary:
    out: OpenLineageRunEventSummary = {}  # type: ignore[typeddict-item]
    if "eventType" in data:
        import aws_sdk_datazone.types.open_lineage_run_state

        out["event_type"] = (
            aws_sdk_datazone.types.open_lineage_run_state.deserialize_json(
                data["eventType"]
            )
        )
    if "runId" in data:
        out["run_id"] = data["runId"]
    if "job" in data:
        import aws_sdk_datazone.types.name_identifier

        out["job"] = aws_sdk_datazone.types.name_identifier.deserialize_json(
            data["job"]
        )
    if "inputs" in data:
        import aws_sdk_datazone.types.name_identifiers

        out["inputs"] = aws_sdk_datazone.types.name_identifiers.deserialize_json(
            data["inputs"]
        )
    if "outputs" in data:
        import aws_sdk_datazone.types.name_identifiers

        out["outputs"] = aws_sdk_datazone.types.name_identifiers.deserialize_json(
            data["outputs"]
        )
    return out
