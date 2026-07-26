"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateSMBFileShareVisibilityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.gateway_arn


class UpdateSMBFileShareVisibilityInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    file_shares_visible: "capo_storage_gateway.types.boolean.Boolean"
    """<p>The shares on this gateway appear when listing shares.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSMBFileShareVisibilityInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["FileSharesVisible"] = value["file_shares_visible"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSMBFileShareVisibilityInput:
    out: UpdateSMBFileShareVisibilityInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError(
            "UpdateSMBFileShareVisibilityInput.gateway_arn required"
        )
    if "FileSharesVisible" in data:
        out["file_shares_visible"] = data["FileSharesVisible"]
    else:
        raise DeserializationError(
            "UpdateSMBFileShareVisibilityInput.file_shares_visible required"
        )
    return out
