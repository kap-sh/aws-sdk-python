"""Generated from Smithy shape ``com.amazonaws.ecs#EphemeralStorage``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer


class EphemeralStorage(TypedDict):
    size_in_gi_b: "aws_sdk_ecs.types.integer.Integer"
    """<p>The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is <code>21</code> GiB and the maximum supported value is <code>200</code> GiB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EphemeralStorage) -> dict:
    out: dict = {}
    out["sizeInGiB"] = value.get("size_in_gi_b", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> EphemeralStorage:
    out: EphemeralStorage = {}  # type: ignore[typeddict-item]
    if "sizeInGiB" in data:
        out["size_in_gi_b"] = data["sizeInGiB"]
    else:
        out["size_in_gi_b"] = 0
    return out
