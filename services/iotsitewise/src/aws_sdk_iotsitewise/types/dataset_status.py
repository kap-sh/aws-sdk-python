"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.dataset_state
    import aws_sdk_iotsitewise.types.error_details


class DatasetStatus(TypedDict):
    state: "aws_sdk_iotsitewise.types.dataset_state.DatasetState"
    """<p>The current status of the dataset.</p>"""
    error: NotRequired["aws_sdk_iotsitewise.types.error_details.ErrorDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetStatus) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.dataset_state

    out["state"] = aws_sdk_iotsitewise.types.dataset_state.serialize_json(
        value["state"]
    )
    if "error" in value:
        import aws_sdk_iotsitewise.types.error_details

        out["error"] = aws_sdk_iotsitewise.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> DatasetStatus:
    out: DatasetStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_iotsitewise.types.dataset_state

        out["state"] = aws_sdk_iotsitewise.types.dataset_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("DatasetStatus.state required")
    if "error" in data:
        import aws_sdk_iotsitewise.types.error_details

        out["error"] = aws_sdk_iotsitewise.types.error_details.deserialize_json(
            data["error"]
        )
    return out
