"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ModelInferencePaymentConfig``."""

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError


class ModelInferencePaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration creator has configured the collaboration member to pay for model inference costs (<code>TRUE</code>) or has not configured the collaboration member to pay for model inference costs (<code>FALSE</code>).</p> <p>Exactly one member can be configured to pay for model inference costs. An error is returned if the collaboration creator sets a <code>TRUE</code> value for more than one member in the collaboration. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for model inference costs, then the member who can query is the default payer. An error is returned if the collaboration creator sets a <code>FALSE</code> value for the member who can query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelInferencePaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> ModelInferencePaymentConfig:
    out: ModelInferencePaymentConfig = {}  # type: ignore[typeddict-item]
    if "isResponsible" in data:
        out["is_responsible"] = data["isResponsible"]
    else:
        raise DeserializationError(
            "ModelInferencePaymentConfig.is_responsible required"
        )
    return out
