"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LoggingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.log_destinations


class LoggingConfiguration(TypedDict):
    destinations: NotRequired[
        "aws_sdk_simspaceweaver.types.log_destinations.LogDestinations"
    ]
    """<p>A list of the locations where SimSpace Weaver sends simulation log data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfiguration) -> dict:
    out: dict = {}
    if "destinations" in value:
        import aws_sdk_simspaceweaver.types.log_destinations

        out["Destinations"] = (
            aws_sdk_simspaceweaver.types.log_destinations.serialize_json(
                value["destinations"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "Destinations" in data:
        import aws_sdk_simspaceweaver.types.log_destinations

        out["destinations"] = (
            aws_sdk_simspaceweaver.types.log_destinations.deserialize_json(
                data["Destinations"]
            )
        )
    return out
