"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclPortRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.ip_port_number_integer

NetworkAclPortRange = TypedDict(
    "NetworkAclPortRange",
    {
        "from": NotRequired[
            "aws_sdk_fms.types.ip_port_number_integer.IPPortNumberInteger"
        ],
        "to": NotRequired[
            "aws_sdk_fms.types.ip_port_number_integer.IPPortNumberInteger"
        ],
    },
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclPortRange) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = value["from"]
    if "to" in value:
        out["To"] = value["to"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAclPortRange:
    out: NetworkAclPortRange = {}  # type: ignore[typeddict-item]
    if "From" in data:
        out["from"] = data["From"]
    if "To" in data:
        out["to"] = data["To"]
    return out
