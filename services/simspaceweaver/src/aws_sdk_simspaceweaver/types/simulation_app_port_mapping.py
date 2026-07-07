"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationAppPortMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.port_number


class SimulationAppPortMapping(TypedDict, closed=True):
    declared: NotRequired["aws_sdk_simspaceweaver.types.port_number.PortNumber"]
    """<p>The TCP/UDP port number of the app, declared in the simulation schema. SimSpace Weaver maps the <code>Declared</code> port to the <code>Actual</code> port. The source code for the app should bind to the <code>Declared</code> port.</p>"""
    actual: NotRequired["aws_sdk_simspaceweaver.types.port_number.PortNumber"]
    """<p>The TCP/UDP port number of the running app. SimSpace Weaver dynamically assigns this port number when the app starts. SimSpace Weaver maps the <code>Declared</code> port to the <code>Actual</code> port. Clients connect to the app using the app's IP address and the <code>Actual</code> port number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimulationAppPortMapping) -> dict:
    out: dict = {}
    if "declared" in value:
        out["Declared"] = value["declared"]
    if "actual" in value:
        out["Actual"] = value["actual"]
    return out


def deserialize_json(data: dict) -> SimulationAppPortMapping:
    out: SimulationAppPortMapping = {}  # type: ignore[typeddict-item]
    if "Declared" in data:
        out["declared"] = data["Declared"]
    if "Actual" in data:
        out["actual"] = data["Actual"]
    return out
