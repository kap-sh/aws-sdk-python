"""Generated from Smithy shape ``com.amazonaws.dataexchange#DeprecationRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.timestamp


class DeprecationRequestDetails(TypedDict, closed=True):
    deprecation_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>A datetime in the future when the data set will be deprecated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeprecationRequestDetails) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.timestamp

    out["DeprecationAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["deprecation_at"]
    )
    return out


def deserialize_json(data: dict) -> DeprecationRequestDetails:
    out: DeprecationRequestDetails = {}  # type: ignore[typeddict-item]
    if "DeprecationAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["deprecation_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["DeprecationAt"]
        )
    else:
        raise DeserializationError("DeprecationRequestDetails.deprecation_at required")
    return out
