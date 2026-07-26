"""Generated from Smithy shape ``com.amazonaws.iot#MetricValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.cidrs
    import capo_iot.types.number
    import capo_iot.types.number_list
    import capo_iot.types.ports
    import capo_iot.types.string_list
    import capo_iot.types.unsigned_long


class MetricValue(TypedDict, closed=True):
    count: NotRequired["capo_iot.types.unsigned_long.UnsignedLong"]
    """<p>If the <code>comparisonOperator</code> calls for a numeric value, use this to specify that numeric value to be compared with the <code>metric</code>.</p>"""
    cidrs: NotRequired["capo_iot.types.cidrs.Cidrs"]
    """<p>If the <code>comparisonOperator</code> calls for a set of CIDRs, use this to specify that set to be compared with the <code>metric</code>.</p>"""
    ports: NotRequired["capo_iot.types.ports.Ports"]
    """<p>If the <code>comparisonOperator</code> calls for a set of ports, use this to specify that set to be compared with the <code>metric</code>.</p>"""
    number: NotRequired["capo_iot.types.number.Number"]
    """<p> The numeral value of a metric. </p>"""
    numbers: NotRequired["capo_iot.types.number_list.NumberList"]
    """<p> The numeral values of a metric. </p>"""
    strings: NotRequired["capo_iot.types.string_list.StringList"]
    """<p> The string values of a metric. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricValue) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "cidrs" in value:
        import capo_iot.types.cidrs

        out["cidrs"] = capo_iot.types.cidrs.serialize_json(value["cidrs"])
    if "ports" in value:
        import capo_iot.types.ports

        out["ports"] = capo_iot.types.ports.serialize_json(value["ports"])
    if "number" in value:
        out["number"] = value["number"]
    if "numbers" in value:
        import capo_iot.types.number_list

        out["numbers"] = capo_iot.types.number_list.serialize_json(value["numbers"])
    if "strings" in value:
        import capo_iot.types.string_list

        out["strings"] = capo_iot.types.string_list.serialize_json(value["strings"])
    return out


def deserialize_json(data: dict) -> MetricValue:
    out: MetricValue = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "cidrs" in data:
        import capo_iot.types.cidrs

        out["cidrs"] = capo_iot.types.cidrs.deserialize_json(data["cidrs"])
    if "ports" in data:
        import capo_iot.types.ports

        out["ports"] = capo_iot.types.ports.deserialize_json(data["ports"])
    if "number" in data:
        out["number"] = data["number"]
    if "numbers" in data:
        import capo_iot.types.number_list

        out["numbers"] = capo_iot.types.number_list.deserialize_json(data["numbers"])
    if "strings" in data:
        import capo_iot.types.string_list

        out["strings"] = capo_iot.types.string_list.deserialize_json(data["strings"])
    return out
