"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.sla_configuration


class SlaContent(TypedDict, closed=True):
    sla_configuration: "aws_sdk_connectcases.types.sla_configuration.SlaConfiguration"
    """<p>Represents an SLA configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlaContent) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.sla_configuration

    out["slaConfiguration"] = (
        aws_sdk_connectcases.types.sla_configuration.serialize_json(
            value["sla_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> SlaContent:
    out: SlaContent = {}  # type: ignore[typeddict-item]
    if "slaConfiguration" in data:
        import aws_sdk_connectcases.types.sla_configuration

        out["sla_configuration"] = (
            aws_sdk_connectcases.types.sla_configuration.deserialize_json(
                data["slaConfiguration"]
            )
        )
    else:
        raise DeserializationError("SlaContent.sla_configuration required")
    return out
