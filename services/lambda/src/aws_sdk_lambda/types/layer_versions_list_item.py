"""Generated from Smithy shape ``com.amazonaws.lambda#LayerVersionsListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.compatible_architectures
    import aws_sdk_lambda.types.compatible_runtimes
    import aws_sdk_lambda.types.description
    import aws_sdk_lambda.types.layer_version_arn
    import aws_sdk_lambda.types.layer_version_number
    import aws_sdk_lambda.types.license_info
    import aws_sdk_lambda.types.timestamp


class LayerVersionsListItem(TypedDict):
    layer_version_arn: NotRequired[
        "aws_sdk_lambda.types.layer_version_arn.LayerVersionArn"
    ]
    """<p>The ARN of the layer version.</p>"""
    version: "aws_sdk_lambda.types.layer_version_number.LayerVersionNumber"
    """<p>The version number.</p>"""
    description: NotRequired["aws_sdk_lambda.types.description.Description"]
    """<p>The description of the version.</p>"""
    created_date: NotRequired["aws_sdk_lambda.types.timestamp.Timestamp"]
    """<p>The date that the version was created, in ISO 8601 format. For example, <code>2018-11-27T15:10:45.123+0000</code>.</p>"""
    compatible_runtimes: NotRequired[
        "aws_sdk_lambda.types.compatible_runtimes.CompatibleRuntimes"
    ]
    """<p>The layer's compatible runtimes.</p> <p>The following list includes deprecated runtimes. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>"""
    license_info: NotRequired["aws_sdk_lambda.types.license_info.LicenseInfo"]
    """<p>The layer's open-source license.</p>"""
    compatible_architectures: NotRequired[
        "aws_sdk_lambda.types.compatible_architectures.CompatibleArchitectures"
    ]
    """<p>A list of compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architectures</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayerVersionsListItem) -> dict:
    out: dict = {}
    if "layer_version_arn" in value:
        out["LayerVersionArn"] = value["layer_version_arn"]
    out["Version"] = value.get("version", 0)
    if "description" in value:
        out["Description"] = value["description"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    if "compatible_runtimes" in value:
        import aws_sdk_lambda.types.compatible_runtimes

        out["CompatibleRuntimes"] = (
            aws_sdk_lambda.types.compatible_runtimes.serialize_json(
                value["compatible_runtimes"]
            )
        )
    if "license_info" in value:
        out["LicenseInfo"] = value["license_info"]
    if "compatible_architectures" in value:
        import aws_sdk_lambda.types.compatible_architectures

        out["CompatibleArchitectures"] = (
            aws_sdk_lambda.types.compatible_architectures.serialize_json(
                value["compatible_architectures"]
            )
        )
    return out


def deserialize_json(data: dict) -> LayerVersionsListItem:
    out: LayerVersionsListItem = {}  # type: ignore[typeddict-item]
    if "LayerVersionArn" in data:
        out["layer_version_arn"] = data["LayerVersionArn"]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedDate" in data:
        out["created_date"] = data["CreatedDate"]
    if "CompatibleRuntimes" in data:
        import aws_sdk_lambda.types.compatible_runtimes

        out["compatible_runtimes"] = (
            aws_sdk_lambda.types.compatible_runtimes.deserialize_json(
                data["CompatibleRuntimes"]
            )
        )
    if "LicenseInfo" in data:
        out["license_info"] = data["LicenseInfo"]
    if "CompatibleArchitectures" in data:
        import aws_sdk_lambda.types.compatible_architectures

        out["compatible_architectures"] = (
            aws_sdk_lambda.types.compatible_architectures.deserialize_json(
                data["CompatibleArchitectures"]
            )
        )
    return out
