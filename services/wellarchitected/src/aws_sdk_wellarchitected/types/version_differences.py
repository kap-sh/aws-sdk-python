"""Generated from Smithy shape ``com.amazonaws.wellarchitected#VersionDifferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.pillar_differences


class VersionDifferences(TypedDict, closed=True):
    pillar_differences: NotRequired[
        "aws_sdk_wellarchitected.types.pillar_differences.PillarDifferences"
    ]
    """<p>The differences between the base and latest versions of the lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionDifferences) -> dict:
    out: dict = {}
    if "pillar_differences" in value:
        import aws_sdk_wellarchitected.types.pillar_differences

        out["PillarDifferences"] = (
            aws_sdk_wellarchitected.types.pillar_differences.serialize_json(
                value["pillar_differences"]
            )
        )
    return out


def deserialize_json(data: dict) -> VersionDifferences:
    out: VersionDifferences = {}  # type: ignore[typeddict-item]
    if "PillarDifferences" in data:
        import aws_sdk_wellarchitected.types.pillar_differences

        out["pillar_differences"] = (
            aws_sdk_wellarchitected.types.pillar_differences.deserialize_json(
                data["PillarDifferences"]
            )
        )
    return out
