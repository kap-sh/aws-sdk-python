"""Generated from Smithy shape ``com.amazonaws.s3#SelectObjectContentEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_s3.errors import DeserializationError, SerializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.records_event
    import aws_sdk_s3.types.stats_event
    import aws_sdk_s3.types.progress_event
    import aws_sdk_s3.types.continuation_event
    import aws_sdk_s3.types.end_event


class _SelectObjectContentEventStream_Records(TypedDict):
    Records: "aws_sdk_s3.types.records_event.RecordsEvent"


class _SelectObjectContentEventStream_Stats(TypedDict):
    Stats: "aws_sdk_s3.types.stats_event.StatsEvent"


class _SelectObjectContentEventStream_Progress(TypedDict):
    Progress: "aws_sdk_s3.types.progress_event.ProgressEvent"


class _SelectObjectContentEventStream_Cont(TypedDict):
    Cont: "aws_sdk_s3.types.continuation_event.ContinuationEvent"


class _SelectObjectContentEventStream_End(TypedDict):
    End: "aws_sdk_s3.types.end_event.EndEvent"


SelectObjectContentEventStream: TypeAlias = (
    _SelectObjectContentEventStream_Records
    | _SelectObjectContentEventStream_Stats
    | _SelectObjectContentEventStream_Progress
    | _SelectObjectContentEventStream_Cont
    | _SelectObjectContentEventStream_End
)


# --- restXml ser/de ---
def serialize_xml(
    value: SelectObjectContentEventStream, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "Records" in value:
        import aws_sdk_s3.types.records_event

        aws_sdk_s3.types.records_event.serialize_xml(value["Records"], el, "Records")
    elif "Stats" in value:
        import aws_sdk_s3.types.stats_event

        aws_sdk_s3.types.stats_event.serialize_xml(value["Stats"], el, "Stats")
    elif "Progress" in value:
        import aws_sdk_s3.types.progress_event

        aws_sdk_s3.types.progress_event.serialize_xml(value["Progress"], el, "Progress")
    elif "Cont" in value:
        import aws_sdk_s3.types.continuation_event

        aws_sdk_s3.types.continuation_event.serialize_xml(value["Cont"], el, "Cont")
    elif "End" in value:
        import aws_sdk_s3.types.end_event

        aws_sdk_s3.types.end_event.serialize_xml(value["End"], el, "End")
    else:
        raise SerializationError("SelectObjectContentEventStream: no variant present")


def deserialize_xml(el: Element) -> SelectObjectContentEventStream:
    for child in el:
        if child.tag == "Records":
            import aws_sdk_s3.types.records_event

            return {"Records": aws_sdk_s3.types.records_event.deserialize_xml(child)}
        elif child.tag == "Stats":
            import aws_sdk_s3.types.stats_event

            return {"Stats": aws_sdk_s3.types.stats_event.deserialize_xml(child)}
        elif child.tag == "Progress":
            import aws_sdk_s3.types.progress_event

            return {"Progress": aws_sdk_s3.types.progress_event.deserialize_xml(child)}
        elif child.tag == "Cont":
            import aws_sdk_s3.types.continuation_event

            return {"Cont": aws_sdk_s3.types.continuation_event.deserialize_xml(child)}
        elif child.tag == "End":
            import aws_sdk_s3.types.end_event

            return {"End": aws_sdk_s3.types.end_event.deserialize_xml(child)}
    raise DeserializationError(
        "SelectObjectContentEventStream: no recognized variant element"
    )
