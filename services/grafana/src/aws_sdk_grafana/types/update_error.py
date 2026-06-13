"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.update_instruction


class UpdateError(TypedDict):
    code: "int"
    """<p>The error code.</p>"""
    message: "str"
    """<p>The message for this error.</p>"""
    caused_by: "aws_sdk_grafana.types.update_instruction.UpdateInstruction"
    """<p>Specifies which permission update caused the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateError) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    import aws_sdk_grafana.types.update_instruction

    out["causedBy"] = aws_sdk_grafana.types.update_instruction.serialize_json(
        value["caused_by"]
    )
    return out


def deserialize_json(data: dict) -> UpdateError:
    out: UpdateError = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("UpdateError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("UpdateError.message required")
    if "causedBy" in data:
        import aws_sdk_grafana.types.update_instruction

        out["caused_by"] = aws_sdk_grafana.types.update_instruction.deserialize_json(
            data["causedBy"]
        )
    else:
        raise DeserializationError("UpdateError.caused_by required")
    return out
