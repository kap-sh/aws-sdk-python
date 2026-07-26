"""Generated from Smithy shape ``com.amazonaws.inspector2#PackageFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.number_filter
    import capo_inspector2.types.string_filter


class PackageFilter(TypedDict, closed=True):
    name: NotRequired["capo_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the name of the package to filter on.</p>"""
    version: NotRequired["capo_inspector2.types.string_filter.StringFilter"]
    """<p>The package version to filter on.</p>"""
    epoch: NotRequired["capo_inspector2.types.number_filter.NumberFilter"]
    """<p>An object that contains details on the package epoch to filter on.</p>"""
    release: NotRequired["capo_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the package release to filter on.</p>"""
    architecture: NotRequired["capo_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the package architecture type to filter on.</p>"""
    source_layer_hash: NotRequired["capo_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the source layer hash to filter on.</p>"""
    source_lambda_layer_arn: NotRequired[
        "capo_inspector2.types.string_filter.StringFilter"
    ]
    """<p>An object that describes the details of a string filter.</p>"""
    file_path: NotRequired["capo_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the package file path to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_inspector2.types.string_filter

        out["name"] = capo_inspector2.types.string_filter.serialize_json(value["name"])
    if "version" in value:
        import capo_inspector2.types.string_filter

        out["version"] = capo_inspector2.types.string_filter.serialize_json(
            value["version"]
        )
    if "epoch" in value:
        import capo_inspector2.types.number_filter

        out["epoch"] = capo_inspector2.types.number_filter.serialize_json(
            value["epoch"]
        )
    if "release" in value:
        import capo_inspector2.types.string_filter

        out["release"] = capo_inspector2.types.string_filter.serialize_json(
            value["release"]
        )
    if "architecture" in value:
        import capo_inspector2.types.string_filter

        out["architecture"] = capo_inspector2.types.string_filter.serialize_json(
            value["architecture"]
        )
    if "source_layer_hash" in value:
        import capo_inspector2.types.string_filter

        out["sourceLayerHash"] = capo_inspector2.types.string_filter.serialize_json(
            value["source_layer_hash"]
        )
    if "source_lambda_layer_arn" in value:
        import capo_inspector2.types.string_filter

        out["sourceLambdaLayerArn"] = (
            capo_inspector2.types.string_filter.serialize_json(
                value["source_lambda_layer_arn"]
            )
        )
    if "file_path" in value:
        import capo_inspector2.types.string_filter

        out["filePath"] = capo_inspector2.types.string_filter.serialize_json(
            value["file_path"]
        )
    return out


def deserialize_json(data: dict) -> PackageFilter:
    out: PackageFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_inspector2.types.string_filter

        out["name"] = capo_inspector2.types.string_filter.deserialize_json(data["name"])
    if "version" in data:
        import capo_inspector2.types.string_filter

        out["version"] = capo_inspector2.types.string_filter.deserialize_json(
            data["version"]
        )
    if "epoch" in data:
        import capo_inspector2.types.number_filter

        out["epoch"] = capo_inspector2.types.number_filter.deserialize_json(
            data["epoch"]
        )
    if "release" in data:
        import capo_inspector2.types.string_filter

        out["release"] = capo_inspector2.types.string_filter.deserialize_json(
            data["release"]
        )
    if "architecture" in data:
        import capo_inspector2.types.string_filter

        out["architecture"] = capo_inspector2.types.string_filter.deserialize_json(
            data["architecture"]
        )
    if "sourceLayerHash" in data:
        import capo_inspector2.types.string_filter

        out["source_layer_hash"] = capo_inspector2.types.string_filter.deserialize_json(
            data["sourceLayerHash"]
        )
    if "sourceLambdaLayerArn" in data:
        import capo_inspector2.types.string_filter

        out["source_lambda_layer_arn"] = (
            capo_inspector2.types.string_filter.deserialize_json(
                data["sourceLambdaLayerArn"]
            )
        )
    if "filePath" in data:
        import capo_inspector2.types.string_filter

        out["file_path"] = capo_inspector2.types.string_filter.deserialize_json(
            data["filePath"]
        )
    return out
