"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateLagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.count
    import aws_sdk_direct_connect.types.encryption_mode
    import aws_sdk_direct_connect.types.lag_id
    import aws_sdk_direct_connect.types.lag_name


class UpdateLagRequest(TypedDict, closed=True):
    lag_id: "aws_sdk_direct_connect.types.lag_id.LagId"
    """<p>The ID of the LAG.</p>"""
    lag_name: NotRequired["aws_sdk_direct_connect.types.lag_name.LagName"]
    """<p>The name of the LAG.</p>"""
    minimum_links: "aws_sdk_direct_connect.types.count.Count"
    """<p>The minimum number of physical connections that must be operational for the LAG itself to be operational.</p>"""
    encryption_mode: NotRequired[
        "aws_sdk_direct_connect.types.encryption_mode.EncryptionMode"
    ]
    """<p>The LAG MAC Security (MACsec) encryption mode.</p> <p>Amazon Web Services applies the value to all connections which are part of the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLagRequest) -> dict:
    out: dict = {}
    out["lagId"] = value["lag_id"]
    if "lag_name" in value:
        out["lagName"] = value["lag_name"]
    out["minimumLinks"] = value.get("minimum_links", 0)
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLagRequest:
    out: UpdateLagRequest = {}  # type: ignore[typeddict-item]
    if "lagId" in data:
        out["lag_id"] = data["lagId"]
    else:
        raise DeserializationError("UpdateLagRequest.lag_id required")
    if "lagName" in data:
        out["lag_name"] = data["lagName"]
    if "minimumLinks" in data:
        out["minimum_links"] = data["minimumLinks"]
    else:
        out["minimum_links"] = 0
    if "encryptionMode" in data:
        out["encryption_mode"] = data["encryptionMode"]
    return out
