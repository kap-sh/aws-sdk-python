"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendAPIConflictResolution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.resolution_strategy


class BackendAPIConflictResolution(TypedDict, closed=True):
    resolution_strategy: NotRequired[
        "aws_sdk_amplifybackend.types.resolution_strategy.ResolutionStrategy"
    ]
    """<p>The strategy for conflict resolution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendAPIConflictResolution) -> dict:
    out: dict = {}
    if "resolution_strategy" in value:
        import aws_sdk_amplifybackend.types.resolution_strategy

        out["resolutionStrategy"] = (
            aws_sdk_amplifybackend.types.resolution_strategy.serialize_json(
                value["resolution_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> BackendAPIConflictResolution:
    out: BackendAPIConflictResolution = {}  # type: ignore[typeddict-item]
    if "resolutionStrategy" in data:
        import aws_sdk_amplifybackend.types.resolution_strategy

        out["resolution_strategy"] = (
            aws_sdk_amplifybackend.types.resolution_strategy.deserialize_json(
                data["resolutionStrategy"]
            )
        )
    return out
