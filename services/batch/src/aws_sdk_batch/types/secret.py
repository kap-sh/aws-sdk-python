"""Generated from Smithy shape ``com.amazonaws.batch#Secret``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class Secret(TypedDict):
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the secret.</p>"""
    value_from: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.</p> <note> <p>If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job you're launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: Secret) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value_from" in value:
        out["valueFrom"] = value["value_from"]
    return out


def deserialize_json(data: dict) -> Secret:
    out: Secret = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "valueFrom" in data:
        out["value_from"] = data["valueFrom"]
    return out
