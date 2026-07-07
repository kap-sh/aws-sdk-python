"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DuplicateTimestamps``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.integer


class DuplicateTimestamps(TypedDict, closed=True):
    total_number_of_duplicate_timestamps: (
        "aws_sdk_lookoutequipment.types.integer.Integer"
    )
    """<p> Indicates the total number of duplicate timestamps. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DuplicateTimestamps) -> dict:
    out: dict = {}
    out["TotalNumberOfDuplicateTimestamps"] = value[
        "total_number_of_duplicate_timestamps"
    ]
    return out


def deserialize_aws_json_1_0(data: dict) -> DuplicateTimestamps:
    out: DuplicateTimestamps = {}  # type: ignore[typeddict-item]
    if "TotalNumberOfDuplicateTimestamps" in data:
        out["total_number_of_duplicate_timestamps"] = data[
            "TotalNumberOfDuplicateTimestamps"
        ]
    else:
        raise DeserializationError(
            "DuplicateTimestamps.total_number_of_duplicate_timestamps required"
        )
    return out
