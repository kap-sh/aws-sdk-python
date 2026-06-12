"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_state
    import aws_sdk_iotsitewise.types.error_details


class AssetModelStatus(TypedDict):
    state: "aws_sdk_iotsitewise.types.asset_model_state.AssetModelState"
    """<p>The current state of the asset model.</p>"""
    error: NotRequired["aws_sdk_iotsitewise.types.error_details.ErrorDetails"]
    """<p>Contains associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelStatus) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_model_state

    out["state"] = aws_sdk_iotsitewise.types.asset_model_state.serialize_json(
        value["state"]
    )
    if "error" in value:
        import aws_sdk_iotsitewise.types.error_details

        out["error"] = aws_sdk_iotsitewise.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> AssetModelStatus:
    out: AssetModelStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_iotsitewise.types.asset_model_state

        out["state"] = aws_sdk_iotsitewise.types.asset_model_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("AssetModelStatus.state required")
    if "error" in data:
        import aws_sdk_iotsitewise.types.error_details

        out["error"] = aws_sdk_iotsitewise.types.error_details.deserialize_json(
            data["error"]
        )
    return out
