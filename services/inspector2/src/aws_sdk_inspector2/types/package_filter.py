"""Generated from Smithy shape ``com.amazonaws.inspector2#PackageFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.number_filter
    import aws_sdk_inspector2.types.string_filter


class PackageFilter(TypedDict):
    name: NotRequired["aws_sdk_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the name of the package to filter on.</p>"""
    version: NotRequired["aws_sdk_inspector2.types.string_filter.StringFilter"]
    """<p>The package version to filter on.</p>"""
    epoch: NotRequired["aws_sdk_inspector2.types.number_filter.NumberFilter"]
    """<p>An object that contains details on the package epoch to filter on.</p>"""
    release: NotRequired["aws_sdk_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the package release to filter on.</p>"""
    architecture: NotRequired["aws_sdk_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the package architecture type to filter on.</p>"""
    source_layer_hash: NotRequired[
        "aws_sdk_inspector2.types.string_filter.StringFilter"
    ]
    """<p>An object that contains details on the source layer hash to filter on.</p>"""
    source_lambda_layer_arn: NotRequired[
        "aws_sdk_inspector2.types.string_filter.StringFilter"
    ]
    """<p>An object that describes the details of a string filter.</p>"""
    file_path: NotRequired["aws_sdk_inspector2.types.string_filter.StringFilter"]
    """<p>An object that contains details on the package file path to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_inspector2.types.string_filter

        out["name"] = aws_sdk_inspector2.types.string_filter.serialize_json(
            value["name"]
        )
    if "version" in value:
        import aws_sdk_inspector2.types.string_filter

        out["version"] = aws_sdk_inspector2.types.string_filter.serialize_json(
            value["version"]
        )
    if "epoch" in value:
        import aws_sdk_inspector2.types.number_filter

        out["epoch"] = aws_sdk_inspector2.types.number_filter.serialize_json(
            value["epoch"]
        )
    if "release" in value:
        import aws_sdk_inspector2.types.string_filter

        out["release"] = aws_sdk_inspector2.types.string_filter.serialize_json(
            value["release"]
        )
    if "architecture" in value:
        import aws_sdk_inspector2.types.string_filter

        out["architecture"] = aws_sdk_inspector2.types.string_filter.serialize_json(
            value["architecture"]
        )
    if "source_layer_hash" in value:
        import aws_sdk_inspector2.types.string_filter

        out["sourceLayerHash"] = aws_sdk_inspector2.types.string_filter.serialize_json(
            value["source_layer_hash"]
        )
    if "source_lambda_layer_arn" in value:
        import aws_sdk_inspector2.types.string_filter

        out["sourceLambdaLayerArn"] = (
            aws_sdk_inspector2.types.string_filter.serialize_json(
                value["source_lambda_layer_arn"]
            )
        )
    if "file_path" in value:
        import aws_sdk_inspector2.types.string_filter

        out["filePath"] = aws_sdk_inspector2.types.string_filter.serialize_json(
            value["file_path"]
        )
    return out


def deserialize_json(data: dict) -> PackageFilter:
    out: PackageFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_inspector2.types.string_filter

        out["name"] = aws_sdk_inspector2.types.string_filter.deserialize_json(
            data["name"]
        )
    if "version" in data:
        import aws_sdk_inspector2.types.string_filter

        out["version"] = aws_sdk_inspector2.types.string_filter.deserialize_json(
            data["version"]
        )
    if "epoch" in data:
        import aws_sdk_inspector2.types.number_filter

        out["epoch"] = aws_sdk_inspector2.types.number_filter.deserialize_json(
            data["epoch"]
        )
    if "release" in data:
        import aws_sdk_inspector2.types.string_filter

        out["release"] = aws_sdk_inspector2.types.string_filter.deserialize_json(
            data["release"]
        )
    if "architecture" in data:
        import aws_sdk_inspector2.types.string_filter

        out["architecture"] = aws_sdk_inspector2.types.string_filter.deserialize_json(
            data["architecture"]
        )
    if "sourceLayerHash" in data:
        import aws_sdk_inspector2.types.string_filter

        out["source_layer_hash"] = (
            aws_sdk_inspector2.types.string_filter.deserialize_json(
                data["sourceLayerHash"]
            )
        )
    if "sourceLambdaLayerArn" in data:
        import aws_sdk_inspector2.types.string_filter

        out["source_lambda_layer_arn"] = (
            aws_sdk_inspector2.types.string_filter.deserialize_json(
                data["sourceLambdaLayerArn"]
            )
        )
    if "filePath" in data:
        import aws_sdk_inspector2.types.string_filter

        out["file_path"] = aws_sdk_inspector2.types.string_filter.deserialize_json(
            data["filePath"]
        )
    return out
