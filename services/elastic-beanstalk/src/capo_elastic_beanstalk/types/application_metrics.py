"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.latency
    import capo_elastic_beanstalk.types.nullable_integer
    import capo_elastic_beanstalk.types.request_count
    import capo_elastic_beanstalk.types.status_codes


class ApplicationMetrics(TypedDict, closed=True):
    duration: NotRequired[
        "capo_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p>The amount of time that the metrics cover (usually 10 seconds). For example, you might have 5 requests (<code>request_count</code>) within the most recent time slice of 10 seconds (<code>duration</code>).</p>"""
    request_count: "capo_elastic_beanstalk.types.request_count.RequestCount"
    """<p>Average number of requests handled by the web server per second over the last 10 seconds.</p>"""
    status_codes: NotRequired["capo_elastic_beanstalk.types.status_codes.StatusCodes"]
    """<p>Represents the percentage of requests over the last 10 seconds that resulted in each type of status code response.</p>"""
    latency: NotRequired["capo_elastic_beanstalk.types.latency.Latency"]
    """<p>Represents the average latency for the slowest X percent of requests over the last 10 seconds. Latencies are in seconds with one millisecond resolution.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationMetrics, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "duration" in value:
        pairs.append((f"{prefix}.Duration", str(value["duration"])))
    pairs.append((f"{prefix}.RequestCount", str(value.get("request_count", 0))))
    if "status_codes" in value:
        import capo_elastic_beanstalk.types.status_codes

        capo_elastic_beanstalk.types.status_codes.serialize_query(
            value["status_codes"], pairs, f"{prefix}.StatusCodes"
        )
    if "latency" in value:
        import capo_elastic_beanstalk.types.latency

        capo_elastic_beanstalk.types.latency.serialize_query(
            value["latency"], pairs, f"{prefix}.Latency"
        )


def deserialize_query(el: Element) -> ApplicationMetrics:
    out: ApplicationMetrics = {}  # type: ignore[typeddict-item]
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_request_count = el.find("RequestCount")
    if child_request_count is not None:
        out["request_count"] = int(child_request_count.text or "")
    else:
        out["request_count"] = 0
    child_status_codes = el.find("StatusCodes")
    if child_status_codes is not None:
        import capo_elastic_beanstalk.types.status_codes

        out["status_codes"] = (
            capo_elastic_beanstalk.types.status_codes.deserialize_query(
                child_status_codes
            )
        )
    child_latency = el.find("Latency")
    if child_latency is not None:
        import capo_elastic_beanstalk.types.latency

        out["latency"] = capo_elastic_beanstalk.types.latency.deserialize_query(
            child_latency
        )
    return out
