"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Latency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.nullable_double


class Latency(TypedDict, closed=True):
    p999: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>The average latency for the slowest 0.1 percent of requests over the last 10 seconds.</p>"""
    p99: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>The average latency for the slowest 1 percent of requests over the last 10 seconds.</p>"""
    p95: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>The average latency for the slowest 5 percent of requests over the last 10 seconds.</p>"""
    p90: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>The average latency for the slowest 10 percent of requests over the last 10 seconds.</p>"""
    p85: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>The average latency for the slowest 15 percent of requests over the last 10 seconds.</p>"""
    p75: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>The average latency for the slowest 25 percent of requests over the last 10 seconds.</p>"""
    p50: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>The average latency for the slowest 50 percent of requests over the last 10 seconds.</p>"""
    p10: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_double.NullableDouble"]
    """<p>The average latency for the slowest 90 percent of requests over the last 10 seconds.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Latency, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "p999" in value:
        pairs.append((f"{prefix}.P999", str(value["p999"])))
    if "p99" in value:
        pairs.append((f"{prefix}.P99", str(value["p99"])))
    if "p95" in value:
        pairs.append((f"{prefix}.P95", str(value["p95"])))
    if "p90" in value:
        pairs.append((f"{prefix}.P90", str(value["p90"])))
    if "p85" in value:
        pairs.append((f"{prefix}.P85", str(value["p85"])))
    if "p75" in value:
        pairs.append((f"{prefix}.P75", str(value["p75"])))
    if "p50" in value:
        pairs.append((f"{prefix}.P50", str(value["p50"])))
    if "p10" in value:
        pairs.append((f"{prefix}.P10", str(value["p10"])))


def deserialize_query(el: Element) -> Latency:
    out: Latency = {}  # type: ignore[typeddict-item]
    child_p999 = el.find("P999")
    if child_p999 is not None:
        out["p999"] = float(child_p999.text or "")
    child_p99 = el.find("P99")
    if child_p99 is not None:
        out["p99"] = float(child_p99.text or "")
    child_p95 = el.find("P95")
    if child_p95 is not None:
        out["p95"] = float(child_p95.text or "")
    child_p90 = el.find("P90")
    if child_p90 is not None:
        out["p90"] = float(child_p90.text or "")
    child_p85 = el.find("P85")
    if child_p85 is not None:
        out["p85"] = float(child_p85.text or "")
    child_p75 = el.find("P75")
    if child_p75 is not None:
        out["p75"] = float(child_p75.text or "")
    child_p50 = el.find("P50")
    if child_p50 is not None:
        out["p50"] = float(child_p50.text or "")
    child_p10 = el.find("P10")
    if child_p10 is not None:
        out["p10"] = float(child_p10.text or "")
    return out
