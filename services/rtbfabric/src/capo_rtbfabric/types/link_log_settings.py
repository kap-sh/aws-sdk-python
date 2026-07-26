"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkLogSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.link_application_log_configuration


class LinkLogSettings(TypedDict, closed=True):
    application_logs: "capo_rtbfabric.types.link_application_log_configuration.LinkApplicationLogConfiguration"
    """<p>Describes the configuration of a link application log.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkLogSettings) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.link_application_log_configuration

    out["applicationLogs"] = (
        capo_rtbfabric.types.link_application_log_configuration.serialize_json(
            value["application_logs"]
        )
    )
    return out


def deserialize_json(data: dict) -> LinkLogSettings:
    out: LinkLogSettings = {}  # type: ignore[typeddict-item]
    if "applicationLogs" in data:
        import capo_rtbfabric.types.link_application_log_configuration

        out["application_logs"] = (
            capo_rtbfabric.types.link_application_log_configuration.deserialize_json(
                data["applicationLogs"]
            )
        )
    else:
        raise DeserializationError("LinkLogSettings.application_logs required")
    return out
