"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetLensVersionDifferenceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.lens_version
    import capo_wellarchitected.types.version_differences


class GetLensVersionDifferenceOutput(TypedDict, closed=True):
    lens_alias: NotRequired["capo_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    base_lens_version: NotRequired[
        "capo_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The base version of the lens.</p>"""
    target_lens_version: NotRequired[
        "capo_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The target lens version for the lens.</p>"""
    latest_lens_version: NotRequired[
        "capo_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The latest version of the lens.</p>"""
    version_differences: NotRequired[
        "capo_wellarchitected.types.version_differences.VersionDifferences"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetLensVersionDifferenceOutput) -> dict:
    out: dict = {}
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "base_lens_version" in value:
        out["BaseLensVersion"] = value["base_lens_version"]
    if "target_lens_version" in value:
        out["TargetLensVersion"] = value["target_lens_version"]
    if "latest_lens_version" in value:
        out["LatestLensVersion"] = value["latest_lens_version"]
    if "version_differences" in value:
        import capo_wellarchitected.types.version_differences

        out["VersionDifferences"] = (
            capo_wellarchitected.types.version_differences.serialize_json(
                value["version_differences"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLensVersionDifferenceOutput:
    out: GetLensVersionDifferenceOutput = {}  # type: ignore[typeddict-item]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "BaseLensVersion" in data:
        out["base_lens_version"] = data["BaseLensVersion"]
    if "TargetLensVersion" in data:
        out["target_lens_version"] = data["TargetLensVersion"]
    if "LatestLensVersion" in data:
        out["latest_lens_version"] = data["LatestLensVersion"]
    if "VersionDifferences" in data:
        import capo_wellarchitected.types.version_differences

        out["version_differences"] = (
            capo_wellarchitected.types.version_differences.deserialize_json(
                data["VersionDifferences"]
            )
        )
    return out
