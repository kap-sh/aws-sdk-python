"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ValidityTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class ValidityTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    agreement_duration: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>The duration of the agreement, in ISO 8601 format.</p>"""
    agreement_end_date: NotRequired["datetime.datetime"]
    """<p>The date when the agreement ends.</p>"""
    agreement_start_date: NotRequired["datetime.datetime"]
    """<p>The date when the agreement starts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidityTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    if "agreement_duration" in value:
        out["agreementDuration"] = value["agreement_duration"]
    if "agreement_end_date" in value:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["agreementEndDate"] = (
            capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["agreement_end_date"]
            )
        )
    if "agreement_start_date" in value:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["agreementStartDate"] = (
            capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["agreement_start_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidityTerm:
    out: ValidityTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ValidityTerm.id required")
    if "type" in data:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ValidityTerm.type required")
    if "agreementDuration" in data:
        out["agreement_duration"] = data["agreementDuration"]
    if "agreementEndDate" in data:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["agreement_end_date"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["agreementEndDate"]
            )
        )
    if "agreementStartDate" in data:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["agreement_start_date"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["agreementStartDate"]
            )
        )
    return out
