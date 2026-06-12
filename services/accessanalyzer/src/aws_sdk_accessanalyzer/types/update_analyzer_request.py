"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UpdateAnalyzerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_configuration
    import aws_sdk_accessanalyzer.types.analyzer_name


class UpdateAnalyzerRequest(TypedDict):
    analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer to modify.</p>"""
    configuration: NotRequired[
        "aws_sdk_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnalyzerRequest) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            aws_sdk_accessanalyzer.types.analyzer_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAnalyzerRequest:
    out: UpdateAnalyzerRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            aws_sdk_accessanalyzer.types.analyzer_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
