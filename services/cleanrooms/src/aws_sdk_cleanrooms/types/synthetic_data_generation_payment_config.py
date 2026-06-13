"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SyntheticDataGenerationPaymentConfig``."""

from typing import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError


class SyntheticDataGenerationPaymentConfig(TypedDict):
    is_responsible: "bool"
    """<p>Indicates who is responsible for paying for synthetic data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataGenerationPaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> SyntheticDataGenerationPaymentConfig:
    out: SyntheticDataGenerationPaymentConfig = {}  # type: ignore[typeddict-item]
    if "isResponsible" in data:
        out["is_responsible"] = data["isResponsible"]
    else:
        raise DeserializationError(
            "SyntheticDataGenerationPaymentConfig.is_responsible required"
        )
    return out
