"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.incremental_refresh


class RefreshConfiguration(TypedDict, closed=True):
    incremental_refresh: (
        "aws_sdk_quicksight.types.incremental_refresh.IncrementalRefresh"
    )
    """<p>The incremental refresh for the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.incremental_refresh

    out["IncrementalRefresh"] = (
        aws_sdk_quicksight.types.incremental_refresh.serialize_json(
            value["incremental_refresh"]
        )
    )
    return out


def deserialize_json(data: dict) -> RefreshConfiguration:
    out: RefreshConfiguration = {}  # type: ignore[typeddict-item]
    if "IncrementalRefresh" in data:
        import aws_sdk_quicksight.types.incremental_refresh

        out["incremental_refresh"] = (
            aws_sdk_quicksight.types.incremental_refresh.deserialize_json(
                data["IncrementalRefresh"]
            )
        )
    else:
        raise DeserializationError("RefreshConfiguration.incremental_refresh required")
    return out
