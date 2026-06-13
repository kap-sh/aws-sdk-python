"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ValidityTerm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_marketplace_discovery.types.bounded_string
    import aws_sdk_marketplace_discovery.types.term_id
    import aws_sdk_marketplace_discovery.types.term_type


class ValidityTerm(TypedDict):
    id: "aws_sdk_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "aws_sdk_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    agreement_duration: NotRequired[
        "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
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
    import aws_sdk_marketplace_discovery.types.term_type

    out["type"] = aws_sdk_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    if "agreement_duration" in value:
        out["agreementDuration"] = value["agreement_duration"]
    if "agreement_end_date" in value:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["agreementEndDate"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["agreement_end_date"]
            )
        )
    if "agreement_start_date" in value:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["agreementStartDate"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.serialize_json(
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
        import aws_sdk_marketplace_discovery.types.term_type

        out["type"] = aws_sdk_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ValidityTerm.type required")
    if "agreementDuration" in data:
        out["agreement_duration"] = data["agreementDuration"]
    if "agreementEndDate" in data:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["agreement_end_date"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["agreementEndDate"]
            )
        )
    if "agreementStartDate" in data:
        import aws_sdk_marketplace_discovery.types._prelude.timestamp

        out["agreement_start_date"] = (
            aws_sdk_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["agreementStartDate"]
            )
        )
    return out
