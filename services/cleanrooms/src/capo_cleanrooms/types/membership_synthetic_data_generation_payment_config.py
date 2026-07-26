"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipSyntheticDataGenerationPaymentConfig``."""

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError


class MembershipSyntheticDataGenerationPaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates if this membership is responsible for paying for synthetic data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSyntheticDataGenerationPaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> MembershipSyntheticDataGenerationPaymentConfig:
    out: MembershipSyntheticDataGenerationPaymentConfig = {}  # type: ignore[typeddict-item]
    if "isResponsible" in data:
        out["is_responsible"] = data["isResponsible"]
    else:
        raise DeserializationError(
            "MembershipSyntheticDataGenerationPaymentConfig.is_responsible required"
        )
    return out
