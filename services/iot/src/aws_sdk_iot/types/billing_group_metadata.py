"""Generated from Smithy shape ``com.amazonaws.iot#BillingGroupMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.creation_date


class BillingGroupMetadata(TypedDict):
    creation_date: NotRequired["aws_sdk_iot.types.creation_date.CreationDate"]
    """<p>The date the billing group was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupMetadata) -> dict:
    out: dict = {}
    if "creation_date" in value:
        import aws_sdk_iot.types.creation_date

        out["creationDate"] = aws_sdk_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> BillingGroupMetadata:
    out: BillingGroupMetadata = {}  # type: ignore[typeddict-item]
    if "creationDate" in data:
        import aws_sdk_iot.types.creation_date

        out["creation_date"] = aws_sdk_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    return out
