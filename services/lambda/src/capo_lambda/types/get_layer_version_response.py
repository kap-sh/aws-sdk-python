"""Generated from Smithy shape ``com.amazonaws.lambda#GetLayerVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.compatible_architectures
    import capo_lambda.types.compatible_runtimes
    import capo_lambda.types.description
    import capo_lambda.types.layer_arn
    import capo_lambda.types.layer_version_arn
    import capo_lambda.types.layer_version_content_output
    import capo_lambda.types.layer_version_number
    import capo_lambda.types.license_info
    import capo_lambda.types.timestamp


class GetLayerVersionResponse(TypedDict, closed=True):
    content: NotRequired[
        "capo_lambda.types.layer_version_content_output.LayerVersionContentOutput"
    ]
    """<p>Details about the layer version.</p>"""
    layer_arn: NotRequired["capo_lambda.types.layer_arn.LayerArn"]
    """<p>The ARN of the layer.</p>"""
    layer_version_arn: NotRequired[
        "capo_lambda.types.layer_version_arn.LayerVersionArn"
    ]
    """<p>The ARN of the layer version.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>The description of the version.</p>"""
    created_date: NotRequired["capo_lambda.types.timestamp.Timestamp"]
    r"""<p>The date that the layer version was created, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    version: "capo_lambda.types.layer_version_number.LayerVersionNumber"
    """<p>The version number.</p>"""
    compatible_architectures: NotRequired[
        "capo_lambda.types.compatible_architectures.CompatibleArchitectures"
    ]
    r"""<p>A list of compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architectures</a>.</p>"""
    compatible_runtimes: NotRequired[
        "capo_lambda.types.compatible_runtimes.CompatibleRuntimes"
    ]
    r"""<p>The layer's compatible runtimes.</p> <p>The following list includes deprecated runtimes. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>"""
    license_info: NotRequired["capo_lambda.types.license_info.LicenseInfo"]
    """<p>The layer's software license.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLayerVersionResponse) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_lambda.types.layer_version_content_output

        out["Content"] = capo_lambda.types.layer_version_content_output.serialize_json(
            value["content"]
        )
    if "layer_arn" in value:
        out["LayerArn"] = value["layer_arn"]
    if "layer_version_arn" in value:
        out["LayerVersionArn"] = value["layer_version_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    out["Version"] = value.get("version", 0)
    if "compatible_architectures" in value:
        import capo_lambda.types.compatible_architectures

        out["CompatibleArchitectures"] = (
            capo_lambda.types.compatible_architectures.serialize_json(
                value["compatible_architectures"]
            )
        )
    if "compatible_runtimes" in value:
        import capo_lambda.types.compatible_runtimes

        out["CompatibleRuntimes"] = (
            capo_lambda.types.compatible_runtimes.serialize_json(
                value["compatible_runtimes"]
            )
        )
    if "license_info" in value:
        out["LicenseInfo"] = value["license_info"]
    return out


def deserialize_json(data: dict) -> GetLayerVersionResponse:
    out: GetLayerVersionResponse = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import capo_lambda.types.layer_version_content_output

        out["content"] = (
            capo_lambda.types.layer_version_content_output.deserialize_json(
                data["Content"]
            )
        )
    if "LayerArn" in data:
        out["layer_arn"] = data["LayerArn"]
    if "LayerVersionArn" in data:
        out["layer_version_arn"] = data["LayerVersionArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedDate" in data:
        out["created_date"] = data["CreatedDate"]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "CompatibleArchitectures" in data:
        import capo_lambda.types.compatible_architectures

        out["compatible_architectures"] = (
            capo_lambda.types.compatible_architectures.deserialize_json(
                data["CompatibleArchitectures"]
            )
        )
    if "CompatibleRuntimes" in data:
        import capo_lambda.types.compatible_runtimes

        out["compatible_runtimes"] = (
            capo_lambda.types.compatible_runtimes.deserialize_json(
                data["CompatibleRuntimes"]
            )
        )
    if "LicenseInfo" in data:
        out["license_info"] = data["LicenseInfo"]
    return out
