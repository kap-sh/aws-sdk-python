"""Generated from Smithy shape ``com.amazonaws.novaact#ModelLifecycle``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.model_status


class ModelLifecycle(TypedDict):
    status: "aws_sdk_nova_act.types.model_status.ModelStatus"
    """<p>The current lifecycle status of the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelLifecycle) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.model_status

    out["status"] = aws_sdk_nova_act.types.model_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> ModelLifecycle:
    out: ModelLifecycle = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_nova_act.types.model_status

        out["status"] = aws_sdk_nova_act.types.model_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ModelLifecycle.status required")
    return out
