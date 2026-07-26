"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceLogEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.string


class ContainerServiceLogEvent(TypedDict, closed=True):
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the container service log event was created.</p>"""
    message: NotRequired["capo_lightsail.types.string.string"]
    """<p>The message of the container service log event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceLogEvent) -> dict:
    out: dict = {}
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceLogEvent:
    out: ContainerServiceLogEvent = {}  # type: ignore[typeddict-item]
    if "createdAt" in data:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
