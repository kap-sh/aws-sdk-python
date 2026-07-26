"""Generated from Smithy shape ``com.amazonaws.managedblockchain#LogConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.log_configuration


class LogConfigurations(TypedDict, closed=True):
    cloudwatch: NotRequired[
        "capo_managedblockchain.types.log_configuration.LogConfiguration"
    ]
    """<p>Parameters for publishing logs to Amazon CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogConfigurations) -> dict:
    out: dict = {}
    if "cloudwatch" in value:
        import capo_managedblockchain.types.log_configuration

        out["Cloudwatch"] = (
            capo_managedblockchain.types.log_configuration.serialize_json(
                value["cloudwatch"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogConfigurations:
    out: LogConfigurations = {}  # type: ignore[typeddict-item]
    if "Cloudwatch" in data:
        import capo_managedblockchain.types.log_configuration

        out["cloudwatch"] = (
            capo_managedblockchain.types.log_configuration.deserialize_json(
                data["Cloudwatch"]
            )
        )
    return out
