"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class DeleteConfigurationRequest(TypedDict, closed=True):
    arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationRequest:
    out: DeleteConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
