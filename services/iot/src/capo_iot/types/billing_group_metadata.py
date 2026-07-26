"""Generated from Smithy shape ``com.amazonaws.iot#BillingGroupMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.creation_date


class BillingGroupMetadata(TypedDict, closed=True):
    creation_date: NotRequired["capo_iot.types.creation_date.CreationDate"]
    """<p>The date the billing group was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupMetadata) -> dict:
    out: dict = {}
    if "creation_date" in value:
        import capo_iot.types.creation_date

        out["creationDate"] = capo_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> BillingGroupMetadata:
    out: BillingGroupMetadata = {}  # type: ignore[typeddict-item]
    if "creationDate" in data:
        import capo_iot.types.creation_date

        out["creation_date"] = capo_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    return out
