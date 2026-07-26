"""Generated from Smithy shape ``com.amazonaws.panorama#NtpPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.ntp_server_list


class NtpPayload(TypedDict, closed=True):
    ntp_servers: "capo_panorama.types.ntp_server_list.NtpServerList"
    """<p>NTP servers to use, in order of preference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NtpPayload) -> dict:
    out: dict = {}
    import capo_panorama.types.ntp_server_list

    out["NtpServers"] = capo_panorama.types.ntp_server_list.serialize_json(
        value["ntp_servers"]
    )
    return out


def deserialize_json(data: dict) -> NtpPayload:
    out: NtpPayload = {}  # type: ignore[typeddict-item]
    if "NtpServers" in data:
        import capo_panorama.types.ntp_server_list

        out["ntp_servers"] = capo_panorama.types.ntp_server_list.deserialize_json(
            data["NtpServers"]
        )
    else:
        raise DeserializationError("NtpPayload.ntp_servers required")
    return out
