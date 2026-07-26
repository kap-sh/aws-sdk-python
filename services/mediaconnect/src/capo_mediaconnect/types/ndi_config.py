"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_ndi_discovery_server_config
    import capo_mediaconnect.types.ndi_state


class NdiConfig(TypedDict, closed=True):
    ndi_state: NotRequired["capo_mediaconnect.types.ndi_state.NdiState"]
    """<p>A setting that controls whether NDI® sources or outputs can be used in the flow. </p> <p> The default value is <code>DISABLED</code>. This value must be set as <code>ENABLED</code> for your flow to support NDI sources or outputs. </p>"""
    machine_name: NotRequired["str"]
    """<p>A prefix for the names of the NDI sources that the flow creates. If a custom name isn't specified, MediaConnect generates a unique 12-character ID as the prefix. </p>"""
    ndi_discovery_servers: NotRequired[
        "capo_mediaconnect.types.__list_of_ndi_discovery_server_config.__listOfNdiDiscoveryServerConfig"
    ]
    """<p>A list of up to three NDI discovery server configurations. While not required by the API, this configuration is necessary for NDI functionality to work properly. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiConfig) -> dict:
    out: dict = {}
    if "ndi_state" in value:
        import capo_mediaconnect.types.ndi_state

        out["ndiState"] = capo_mediaconnect.types.ndi_state.serialize_json(
            value["ndi_state"]
        )
    if "machine_name" in value:
        out["machineName"] = value["machine_name"]
    if "ndi_discovery_servers" in value:
        import capo_mediaconnect.types.__list_of_ndi_discovery_server_config

        out["ndiDiscoveryServers"] = (
            capo_mediaconnect.types.__list_of_ndi_discovery_server_config.serialize_json(
                value["ndi_discovery_servers"]
            )
        )
    return out


def deserialize_json(data: dict) -> NdiConfig:
    out: NdiConfig = {}  # type: ignore[typeddict-item]
    if "ndiState" in data:
        import capo_mediaconnect.types.ndi_state

        out["ndi_state"] = capo_mediaconnect.types.ndi_state.deserialize_json(
            data["ndiState"]
        )
    if "machineName" in data:
        out["machine_name"] = data["machineName"]
    if "ndiDiscoveryServers" in data:
        import capo_mediaconnect.types.__list_of_ndi_discovery_server_config

        out["ndi_discovery_servers"] = (
            capo_mediaconnect.types.__list_of_ndi_discovery_server_config.deserialize_json(
                data["ndiDiscoveryServers"]
            )
        )
    return out
