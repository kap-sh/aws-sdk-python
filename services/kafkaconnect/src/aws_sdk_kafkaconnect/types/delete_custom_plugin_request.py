"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteCustomPluginRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class DeleteCustomPluginRequest(TypedDict, closed=True):
    custom_plugin_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the custom plugin that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomPluginRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomPluginRequest:
    out: DeleteCustomPluginRequest = {}  # type: ignore[typeddict-item]
    return out
