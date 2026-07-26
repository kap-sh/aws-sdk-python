"""Generated from Smithy shape ``com.amazonaws.internetmonitor#Network``."""

from typing_extensions import TypedDict

from capo_internetmonitor.errors import DeserializationError


class Network(TypedDict, closed=True):
    as_name: "str"
    """<p>The name of the internet service provider (ISP) or network (ASN).</p>"""
    as_number: "int"
    """<p>The Autonomous System Number (ASN) of the internet provider or network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Network) -> dict:
    out: dict = {}
    out["ASName"] = value["as_name"]
    out["ASNumber"] = value["as_number"]
    return out


def deserialize_json(data: dict) -> Network:
    out: Network = {}  # type: ignore[typeddict-item]
    if "ASName" in data:
        out["as_name"] = data["ASName"]
    else:
        raise DeserializationError("Network.as_name required")
    if "ASNumber" in data:
        out["as_number"] = data["ASNumber"]
    else:
        raise DeserializationError("Network.as_number required")
    return out
