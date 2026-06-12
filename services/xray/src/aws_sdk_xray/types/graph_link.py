"""Generated from Smithy shape ``com.amazonaws.xray#GraphLink``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.trace_id_list


class GraphLink(TypedDict):
    reference_type: NotRequired["aws_sdk_xray.types.string.String"]
    """<p> Relationship of a trace to the corresponding service. </p>"""
    source_trace_id: NotRequired["aws_sdk_xray.types.string.String"]
    """<p> Source trace of a link relationship. </p>"""
    destination_trace_ids: NotRequired["aws_sdk_xray.types.trace_id_list.TraceIdList"]
    """<p> Destination traces of a link relationship. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GraphLink) -> dict:
    out: dict = {}
    if "reference_type" in value:
        out["ReferenceType"] = value["reference_type"]
    if "source_trace_id" in value:
        out["SourceTraceId"] = value["source_trace_id"]
    if "destination_trace_ids" in value:
        import aws_sdk_xray.types.trace_id_list

        out["DestinationTraceIds"] = aws_sdk_xray.types.trace_id_list.serialize_json(
            value["destination_trace_ids"]
        )
    return out


def deserialize_json(data: dict) -> GraphLink:
    out: GraphLink = {}  # type: ignore[typeddict-item]
    if "ReferenceType" in data:
        out["reference_type"] = data["ReferenceType"]
    if "SourceTraceId" in data:
        out["source_trace_id"] = data["SourceTraceId"]
    if "DestinationTraceIds" in data:
        import aws_sdk_xray.types.trace_id_list

        out["destination_trace_ids"] = (
            aws_sdk_xray.types.trace_id_list.deserialize_json(
                data["DestinationTraceIds"]
            )
        )
    return out
