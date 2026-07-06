"""Generated from Smithy shape ``com.amazonaws.dax#SSESpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dax.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dax.types.sse_enabled


class SSESpecification(TypedDict, closed=True):
    enabled: "aws_sdk_dax.types.sse_enabled.SSEEnabled"
    """<p>Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SSESpecification) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SSESpecification:
    out: SSESpecification = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("SSESpecification.enabled required")
    return out
