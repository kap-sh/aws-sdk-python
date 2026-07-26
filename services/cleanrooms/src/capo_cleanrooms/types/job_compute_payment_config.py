"""Generated from Smithy shape ``com.amazonaws.cleanrooms#JobComputePaymentConfig``."""

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError


class JobComputePaymentConfig(TypedDict, closed=True):
    is_responsible: "bool"
    """<p>Indicates whether the collaboration creator has configured the collaboration member to pay for query and job compute costs (<code>TRUE</code>) or has not configured the collaboration member to pay for query and job compute costs (<code>FALSE</code>).</p> <p>Exactly one member can be configured to pay for query and job compute costs. An error is returned if the collaboration creator sets a <code>TRUE</code> value for more than one member in the collaboration. </p> <p>An error is returned if the collaboration creator sets a <code>FALSE</code> value for the member who can run queries and jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobComputePaymentConfig) -> dict:
    out: dict = {}
    out["isResponsible"] = value["is_responsible"]
    return out


def deserialize_json(data: dict) -> JobComputePaymentConfig:
    out: JobComputePaymentConfig = {}  # type: ignore[typeddict-item]
    if "isResponsible" in data:
        out["is_responsible"] = data["isResponsible"]
    else:
        raise DeserializationError("JobComputePaymentConfig.is_responsible required")
    return out
