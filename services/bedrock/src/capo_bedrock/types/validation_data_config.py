"""Generated from Smithy shape ``com.amazonaws.bedrock#ValidationDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.validators


class ValidationDataConfig(TypedDict, closed=True):
    validators: "capo_bedrock.types.validators.Validators"
    """<p>Information about the validators.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationDataConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.validators

    out["validators"] = capo_bedrock.types.validators.serialize_json(
        value["validators"]
    )
    return out


def deserialize_json(data: dict) -> ValidationDataConfig:
    out: ValidationDataConfig = {}  # type: ignore[typeddict-item]
    if "validators" in data:
        import capo_bedrock.types.validators

        out["validators"] = capo_bedrock.types.validators.deserialize_json(
            data["validators"]
        )
    else:
        raise DeserializationError("ValidationDataConfig.validators required")
    return out
