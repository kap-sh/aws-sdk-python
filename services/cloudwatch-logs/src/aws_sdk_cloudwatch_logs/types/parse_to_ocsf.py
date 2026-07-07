"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ParseToOCSF``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.event_source
    import aws_sdk_cloudwatch_logs.types.mapping_version
    import aws_sdk_cloudwatch_logs.types.ocsf_version
    import aws_sdk_cloudwatch_logs.types.source


class ParseToOCSF(TypedDict, closed=True):
    source: NotRequired["aws_sdk_cloudwatch_logs.types.source.Source"]
    """<p>The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.</p>"""
    event_source: "aws_sdk_cloudwatch_logs.types.event_source.EventSource"
    """<p>Specify the service or process that produces the log events that will be converted with this processor.</p>"""
    ocsf_version: "aws_sdk_cloudwatch_logs.types.ocsf_version.OCSFVersion"
    """<p>Specify which version of the OCSF schema to use for the transformed log events.</p>"""
    mapping_version: NotRequired[
        "aws_sdk_cloudwatch_logs.types.mapping_version.MappingVersion"
    ]
    """<p>The version of the OCSF mapping to use for parsing log data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParseToOCSF) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    import aws_sdk_cloudwatch_logs.types.event_source

    out["eventSource"] = (
        aws_sdk_cloudwatch_logs.types.event_source.serialize_aws_json_1_1(
            value["event_source"]
        )
    )
    import aws_sdk_cloudwatch_logs.types.ocsf_version

    out["ocsfVersion"] = (
        aws_sdk_cloudwatch_logs.types.ocsf_version.serialize_aws_json_1_1(
            value["ocsf_version"]
        )
    )
    if "mapping_version" in value:
        out["mappingVersion"] = value["mapping_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParseToOCSF:
    out: ParseToOCSF = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    if "eventSource" in data:
        import aws_sdk_cloudwatch_logs.types.event_source

        out["event_source"] = (
            aws_sdk_cloudwatch_logs.types.event_source.deserialize_aws_json_1_1(
                data["eventSource"]
            )
        )
    else:
        raise DeserializationError("ParseToOCSF.event_source required")
    if "ocsfVersion" in data:
        import aws_sdk_cloudwatch_logs.types.ocsf_version

        out["ocsf_version"] = (
            aws_sdk_cloudwatch_logs.types.ocsf_version.deserialize_aws_json_1_1(
                data["ocsfVersion"]
            )
        )
    else:
        raise DeserializationError("ParseToOCSF.ocsf_version required")
    if "mappingVersion" in data:
        out["mapping_version"] = data["mappingVersion"]
    return out
