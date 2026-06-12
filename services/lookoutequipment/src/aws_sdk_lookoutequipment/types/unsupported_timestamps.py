"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UnsupportedTimestamps``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.integer


class UnsupportedTimestamps(TypedDict):
    total_number_of_unsupported_timestamps: (
        "aws_sdk_lookoutequipment.types.integer.Integer"
    )
    """<p> Indicates the total number of unsupported timestamps across the ingested data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnsupportedTimestamps) -> dict:
    out: dict = {}
    out["TotalNumberOfUnsupportedTimestamps"] = value[
        "total_number_of_unsupported_timestamps"
    ]
    return out


def deserialize_aws_json_1_0(data: dict) -> UnsupportedTimestamps:
    out: UnsupportedTimestamps = {}  # type: ignore[typeddict-item]
    if "TotalNumberOfUnsupportedTimestamps" in data:
        out["total_number_of_unsupported_timestamps"] = data[
            "TotalNumberOfUnsupportedTimestamps"
        ]
    else:
        raise DeserializationError(
            "UnsupportedTimestamps.total_number_of_unsupported_timestamps required"
        )
    return out
