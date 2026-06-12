"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListMetricStreamsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.metric_stream_entries
    import aws_sdk_cloudwatch.types.next_token


class ListMetricStreamsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results. You can use this token in a subsequent operation to get the next batch of results.</p>"""
    entries: NotRequired[
        "aws_sdk_cloudwatch.types.metric_stream_entries.MetricStreamEntries"
    ]
    """<p>The array of metric stream information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMetricStreamsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "entries" in value:
        import aws_sdk_cloudwatch.types.metric_stream_entries

        out["Entries"] = (
            aws_sdk_cloudwatch.types.metric_stream_entries.serialize_aws_json_1_0(
                value["entries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMetricStreamsOutput:
    out: ListMetricStreamsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Entries" in data:
        import aws_sdk_cloudwatch.types.metric_stream_entries

        out["entries"] = (
            aws_sdk_cloudwatch.types.metric_stream_entries.deserialize_aws_json_1_0(
                data["Entries"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListMetricStreamsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "entries" in value:
        import aws_sdk_cloudwatch.types.metric_stream_entries

        aws_sdk_cloudwatch.types.metric_stream_entries.serialize_query(
            value["entries"], pairs, f"{prefix}.Entries"
        )


def deserialize_query(el: Element) -> ListMetricStreamsOutput:
    out: ListMetricStreamsOutput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_entries = el.find("Entries")
    if child_entries is not None:
        import aws_sdk_cloudwatch.types.metric_stream_entries

        out["entries"] = (
            aws_sdk_cloudwatch.types.metric_stream_entries.deserialize_query(
                child_entries
            )
        )
    return out
