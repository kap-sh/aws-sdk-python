"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ModelTrainingPaymentConfig``."""

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError


class ModelTrainingPaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration creator has configured the collaboration member to pay for model training costs (<code>TRUE</code>) or has not configured the collaboration member to pay for model training costs (<code>FALSE</code>).</p> <p>Exactly one member can be configured to pay for model training costs. An error is returned if the collaboration creator sets a <code>TRUE</code> value for more than one member in the collaboration. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for model training costs, then the member who can query is the default payer. An error is returned if the collaboration creator sets a <code>FALSE</code> value for the member who can query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelTrainingPaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> ModelTrainingPaymentConfig:
    out: ModelTrainingPaymentConfig = {}  # type: ignore[typeddict-item]
    if "isResponsible" in data:
        out["is_responsible"] = data["isResponsible"]
    else:
        raise DeserializationError("ModelTrainingPaymentConfig.is_responsible required")
    return out
